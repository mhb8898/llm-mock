from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    id: str
    created_at: datetime
    role: str
    content: str

class Interaction(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    settings: dict
    messages: List[Message]
