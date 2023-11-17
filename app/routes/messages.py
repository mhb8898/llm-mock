"""Module for handling message-related routes in the FastAPI application.

This module contains endpoints for creating new messages within interactions and
for retrieving all messages from a specific interaction.
"""
from uuid import uuid4
from datetime import datetime
from fastapi import APIRouter, HTTPException
from ..models import Message
from .data_store import get_data_store

data_store = get_data_store()

router = APIRouter()


@router.post("/interactions/{interaction_id}/messages")
async def create_message(interaction_id: str, content: str, role: str):
    """Create a new message in a specific interaction.

    Args:
        ... (describe your arguments here)

    Returns:
        ... (describe the return value)
    """
    if interaction_id not in data_store.interactions:
        raise HTTPException(status_code=404, detail="Interaction not found")

    message_id = str(uuid4())
    message = Message(id=message_id, created_at=datetime.now(), role=role, content=content)
    data_store.interactions[interaction_id].messages.append(message)
    data_store.interactions[interaction_id].updated_at = datetime.now()

    return message


@router.get("/interactions/{interaction_id}/messages")
async def get_all_messages(interaction_id: str):
    """Retrieve all messages from a specific interaction.

    Args:
        ... (describe your arguments here)

    Returns:
        ... (describe the return value)
    """
    if interaction_id not in data_store.interactions:
        raise HTTPException(status_code=404, detail="Interaction not found")

    return data_store.interactions[interaction_id].messages
