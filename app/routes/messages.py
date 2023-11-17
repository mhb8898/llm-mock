from fastapi import APIRouter, HTTPException
from ..models import Message
from uuid import uuid4
from datetime import datetime
from .data_store import get_data_store

data_store = get_data_store()

router = APIRouter()


@router.post("/interactions/{interaction_id}/messages")
async def create_message(interaction_id: str, content: str, role: str):
    if interaction_id not in data_store.interactions:
        raise HTTPException(status_code=404, detail="Interaction not found")

    message_id = str(uuid4())
    message = Message(
        id=message_id, created_at=datetime.now(), role=role, content=content
    )
    data_store.interactions[interaction_id].messages.append(message)
    data_store.interactions[interaction_id].updated_at = datetime.now()

    return message


@router.get("/interactions/{interaction_id}/messages")
async def get_all_messages(interaction_id: str):
    if interaction_id not in data_store.interactions:
        raise HTTPException(status_code=404, detail="Interaction not found")

    return data_store.interactions[interaction_id].messages
