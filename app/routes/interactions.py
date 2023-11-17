from fastapi import APIRouter, HTTPException
from ..models import Interaction
from uuid import uuid4
from datetime import datetime
from .data_store import get_data_store

data_store = get_data_store()


router = APIRouter()

@router.post("/interactions")
async def create_interaction(settings: dict):
    interaction_id = str(uuid4())
    now = datetime.now()
    interaction = Interaction(
        id=interaction_id,
        created_at=now,
        updated_at=now,
        settings=settings,
        messages=[]
    )
    data_store.interactions[interaction_id] = interaction
    return interaction

@router.get("/interactions")
async def get_all_interactions():
    return list(data_store.interactions.values())
