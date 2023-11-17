"""Module for managing interaction routes in a FastAPI application.

This module contains routes for creating and managing interactions...
"""

from uuid import uuid4
from datetime import datetime
from fastapi import APIRouter
from ..models import Interaction
from .data_store import get_data_store

data_store = get_data_store()


router = APIRouter()


@router.post("/interactions")
async def create_interaction(settings: dict):
    """
    Create a new interaction with the given settings and return it.

    This endpoint generates a unique ID for the new interaction, sets the creation and
    update timestamps to the current time, and stores the interaction in the data store.
    Initially, the interaction will have no messages.

    Args:
        settings (dict): A dictionary containing the configuration or settings for the interaction.

    Returns:
        Interaction: The newly created interaction object.
    """
    interaction_id = str(uuid4())
    now = datetime.now()
    interaction = Interaction(
        id=interaction_id,
        created_at=now,
        updated_at=now,
        settings=settings,
        messages=[],
    )
    data_store.interactions[interaction_id] = interaction
    return interaction


@router.get("/interactions")
async def get_all_interactions():
    """
    Retrieve and return a list of all interaction objects.

    This endpoint fetches all stored interactions from the data store and returns them as a list.
    It's useful for getting an overview of all interactions that have occurred.

    Returns:
        List[Interaction]: A list of all interaction objects.
    """
    return list(data_store.interactions.values())
