from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from week2.app.main import create_app
from week2.app.routers import notes
from week2.app.services.extract import extract_action_items


def test_rules_extract_marked_items_only():
    text = "Meeting notes\n- [ ] Write tests\nTODO: Review docs\n- [x] Done\n- Write tests"
    assert extract_action_items(text) == ["Write tests", "Review docs"]


def test_homepage_and_preview_do_not_create_db(tmp_path):
    path = tmp_path / "app.db"
    client = TestClient(create_app(path))
    home = client.get("/")
    assert home.status_code == 200
    assert 'id="extract-llm"' in home.text
    result = client.post("/action-items/extract", json={"text": "- Write tests"})
    assert result.status_code == 200
    assert result.json() == {"items": ["Write tests"], "note_id": None}
    assert client.get("/notes").json() == []
    assert not path.exists()


def test_blank_input_is_rejected_without_saving(tmp_path):
    path = tmp_path / "app.db"
    client = TestClient(create_app(path))
    result = client.post("/action-items/extract", json={"text": "  ", "save_note": True})
    assert result.status_code == 400
    assert not path.exists()


def test_confirmed_notes_are_read_in_reverse_insert_order(tmp_path):
    path = tmp_path / "app.db"
    client = TestClient(create_app(path))
    for note in ("Meeting A\n- Write tests", "Meeting B\n- Review docs"):
        result = client.post("/action-items/extract", json={"text": note, "save_note": True})
        assert result.status_code == 200
    reopened = TestClient(create_app(path))
    assert reopened.get("/notes").json() == [
        {"id": 2, "content": "Meeting B\n- Review docs"},
        {"id": 1, "content": "Meeting A\n- Write tests"},
    ]


def test_llm_route_only_saves_when_requested(tmp_path, monkeypatch):
    model = Mock(return_value=["Write tests"])
    monkeypatch.setattr(notes, "extract_action_items_llm", model)
    path = tmp_path / "app.db"
    client = TestClient(create_app(path))
    endpoint = "/action-items/extract-llm"
    assert client.post(endpoint, json={"text": "  "}).status_code == 400
    model.assert_not_called()

    text = "We agreed to write tests."
    preview = client.post(endpoint, json={"text": text})
    assert preview.status_code == 200
    assert preview.json() == {"items": ["Write tests"], "note_id": None}
    model.assert_called_once_with(text)
    assert not path.exists()

    saved = client.post(endpoint, json={"text": text, "save_note": True})
    assert saved.status_code == 200
    assert saved.json() == {"items": ["Write tests"], "note_id": 1}
    assert client.get("/notes").json() == [{"id": 1, "content": text}]


@pytest.mark.parametrize(
    ("failure", "status", "detail"),
    [
        (notes.QwenUnavailableError("Qwen request failed."), 503, "Qwen request failed."),
        (ValueError("private upstream detail"), 502, "Invalid Qwen response"),
    ],
)
def test_llm_failure_does_not_fallback_or_save(tmp_path, monkeypatch, failure, status, detail):
    model = Mock(side_effect=failure)
    rules = Mock()
    monkeypatch.setattr(notes, "extract_action_items_llm", model)
    monkeypatch.setattr(notes, "extract_action_items", rules)
    path = tmp_path / "app.db"
    client = TestClient(create_app(path))
    response = client.post(
        "/action-items/extract-llm", json={"text": "- Write tests", "save_note": True}
    )
    assert response.status_code == status
    assert response.json() == {"detail": detail}
    assert "private upstream detail" not in response.text
    rules.assert_not_called()
    assert not path.exists()
