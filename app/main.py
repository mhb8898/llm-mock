"""
This module is the entry point for a FastAPI application designed for
AI-powered chat interactions. 

The application includes routes for managing chat interactions and
messages. These routes are defined in separate modules and included
in the FastAPI application instance.

Routes:
- Interactions: Handles the creation and retrieval of chat interactions.
Each interaction can encompass multiple messages and is uniquely identified.
- Messages: Manages the individual messages within a specific interaction.
This includes adding new messages and fetching existing messages.

The application is structured to use FastAPI's ability to organize
routes via routers, promoting modularity and maintainability.
"""
from fastapi import FastAPI
from .routes import interactions, messages

app = FastAPI()

app.include_router(interactions.router)
app.include_router(messages.router)
