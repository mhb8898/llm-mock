from fastapi import FastAPI
from .routes import interactions, messages

app = FastAPI()

app.include_router(interactions.router)
app.include_router(messages.router)
