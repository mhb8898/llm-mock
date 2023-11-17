"""
This module defines the data models used for handling chat interactions
in an AI-powered chat application.

Classes:
- Message: Represents a single message within an interaction. It includes
details such as the message ID, creation timestamp, the role of the sender
(e.g., human, bot), and the content of the message.
- Interaction: Represents an entire interaction session. It includes the
interaction ID, creation and update timestamps, specific settings for the
interaction, and a list of all messages that form part of this interaction.

These models are built using Pydantic, which provides automatic data
validation, serialization, and (de)serialization from and to JSON objects.
This ensures that data exchanged between the server and clients is consistent
and adheres to the defined schema.
"""

from typing import List
from datetime import datetime
from pydantic import BaseModel


# pylint: disable=R0903
class Message(BaseModel):
    """
    Represents a message in the context of an interaction.

    Attributes:
    - id (str): A unique identifier for the message.
    - created_at (datetime): The timestamp when the message was created.
    - role (str): The role of the message sender, e.g., 'user', 'bot'.
    - content (str): The actual text content of the message.
    """

    id: str
    created_at: datetime
    role: str
    content: str


# pylint: disable=R0903
class Interaction(BaseModel):
    """
    Represents an interaction session, which consists of multiple messages.

    Attributes:
    - id (str): A unique identifier for the interaction.
    - created_at (datetime): The timestamp when the interaction was created.
    - updated_at (datetime): The timestamp when the interaction was last updated.
    - settings (dict): A dictionary of settings/configurations for the interaction.
    - messages (List[Message]): A list of messages that are part of the interaction.
    """

    id: str
    created_at: datetime
    updated_at: datetime
    settings: dict
    messages: List[Message]
