from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

from ..db import list_notes, save_note
from ..services.extract import QwenUnavailableError, extract_action_items, extract_action_items_llm

router = APIRouter()


class ExtractRequest(BaseModel):
    text: str = Field(max_length=10000)
    save_note: bool = False


@router.post("/action-items/extract")
def extract(payload: ExtractRequest, request: Request):
    return _extract(payload, request, use_llm=False)


@router.post("/action-items/extract-llm")
def extract_llm(payload: ExtractRequest, request: Request):
    return _extract(payload, request, use_llm=True)


def _extract(payload: ExtractRequest, request: Request, *, use_llm: bool):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Note text cannot be empty")
    if use_llm:
        try:
            items = extract_action_items_llm(payload.text)
        except QwenUnavailableError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        except ValueError as exc:
            raise HTTPException(status_code=502, detail="Invalid Qwen response") from exc
    else:
        items = extract_action_items(payload.text)
    note_id = save_note(request.app.state.db_path, payload.text) if payload.save_note else None
    return {"items": items, "note_id": note_id}


@router.get("/notes")
def notes(request: Request):
    return list_notes(request.app.state.db_path)
