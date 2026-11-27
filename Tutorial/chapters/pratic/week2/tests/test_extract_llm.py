from types import SimpleNamespace
from unittest.mock import MagicMock

import httpx
import pytest
from openai import APIStatusError, APITimeoutError

from week2.app.services import extract


@pytest.fixture
def qwen(monkeypatch):
    monkeypatch.setenv("DASHSCOPE_API_KEY", "test-key")
    monkeypatch.setenv("DASHSCOPE_MODEL", "test-model")
    monkeypatch.delenv("DASHSCOPE_BASE_URL", raising=False)
    client = MagicMock()
    create = client.return_value.__enter__.return_value.chat.completions.create
    monkeypatch.setattr(extract, "OpenAI", client)
    return client, create


def tool_response(arguments, name="submit_action_items"):
    return {
        "choices": [
            {"message": {"tool_calls": [{"function": {"name": name, "arguments": arguments}}]}}
        ]
    }


def test_blank_input_does_not_create_client(qwen, monkeypatch):
    client, _ = qwen
    monkeypatch.delenv("DASHSCOPE_API_KEY")
    monkeypatch.delenv("DASHSCOPE_MODEL")
    assert extract.extract_action_items_llm(" \n ") == []
    client.assert_not_called()


@pytest.mark.parametrize("variable", ["DASHSCOPE_API_KEY", "DASHSCOPE_MODEL"])
def test_missing_config_does_not_create_client(qwen, monkeypatch, variable):
    client, _ = qwen
    monkeypatch.delenv(variable)
    with pytest.raises(extract.QwenUnavailableError, match="DASHSCOPE_API_KEY and DASHSCOPE_MODEL"):
        extract.extract_action_items_llm("Write tests")
    client.assert_not_called()


def test_object_response_and_tool_schema(qwen):
    client, create = qwen
    function = SimpleNamespace(
        name="submit_action_items",
        arguments='{"action_items": [" Write tests ", "", "write tests", "Review docs"]}',
    )
    message = SimpleNamespace(tool_calls=[SimpleNamespace(function=function)])
    create.return_value = SimpleNamespace(choices=[SimpleNamespace(message=message)])

    assert extract.extract_action_items_llm(" Write tests and review docs. ") == [
        "Write tests",
        "Review docs",
    ]
    assert client.call_args.kwargs["base_url"] == "https://dashscope.aliyuncs.com/compatible-mode/v1"
    assert client.call_args.kwargs["api_key"] == "test-key"
    assert client.call_args.kwargs["max_retries"] == 0
    create.assert_called_once()
    request = create.call_args.kwargs
    assert request["model"] == "test-model"
    assert request["tool_choice"] == "auto"
    assert request["extra_body"] == {"enable_thinking": False}
    assert request["messages"][-1] == {"role": "user", "content": "Write tests and review docs."}
    schema = request["tools"][0]["function"]["parameters"]
    assert schema["required"] == ["action_items"]
    assert schema["properties"]["action_items"] == {"type": "array", "items": {"type": "string"}}


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [
        ('```json\n{"action_items": ["Write tests"]}\n```', ["Write tests"]),
        ({"action_items": []}, []),
    ],
)
def test_dictionary_response(qwen, arguments, expected):
    _, create = qwen
    create.return_value = tool_response(arguments)
    assert extract.extract_action_items_llm("Meeting notes") == expected


def test_workspace_base_url_override(qwen, monkeypatch):
    client, create = qwen
    base_url = "https://workspace.example.invalid/compatible-mode/v1"
    monkeypatch.setenv("DASHSCOPE_BASE_URL", base_url)
    create.return_value = tool_response({"action_items": []})

    assert extract.extract_action_items_llm("Meeting notes") == []
    assert client.call_args.kwargs["base_url"] == base_url


@pytest.mark.parametrize(
    ("response", "error"),
    [
        (tool_response("{invalid"), "not valid JSON"),
        (tool_response('{"action_items": [42]}'), "array of strings"),
        (tool_response('{"items": []}'), "array of strings"),
        (tool_response('{"action_items": [], "extra": 1}'), "array of strings"),
        ({"choices": [{"message": {"content": '{"action_items": []}'}}]}, "tool call"),
        (tool_response('{"action_items": []}', name="unexpected"), "tool call"),
    ],
)
def test_invalid_response_raises_without_fallback(qwen, response, error):
    _, create = qwen
    create.return_value = response
    with pytest.raises(ValueError, match=error):
        extract.extract_action_items_llm("- Write tests")


@pytest.mark.parametrize(
    "failure",
    [
        APITimeoutError(httpx.Request("POST", "https://example.invalid")),
        APIStatusError(
            "private upstream detail",
            response=httpx.Response(429, request=httpx.Request("POST", "https://example.invalid")),
            body={"message": "private upstream detail"},
        ),
    ],
)
def test_request_failure_raises_without_fallback(qwen, failure):
    _, create = qwen
    create.side_effect = failure
    with pytest.raises(extract.QwenUnavailableError, match=r"^Qwen request failed\.$"):
        extract.extract_action_items_llm("- Write tests")
    create.assert_called_once()
