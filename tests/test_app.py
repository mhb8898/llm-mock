"""
This module contains test cases for the FastAPI application.

It includes tests for various API endpoints to ensure that the application behaves as expected 
when handling requests for creating and retrieving interactions and messages.
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_interaction():
    """
    Test the creation of a new interaction.

    This test ensures that posting to the '/interactions' endpoint with valid settings
    successfully creates a new interaction and returns the correct data,
    including a unique interaction ID and the specified settings.
    """
    response = client.post("/interactions", json={"model_name": "GPT4", "role": "System"})
    assert response.status_code == 200
    data = response.json()
    assert data["settings"]["model_name"] == "GPT4"
    assert "id" in data


def test_get_all_interactions():
    """
    Test retrieving all interactions.

    This test checks that a GET request to the '/interactions' endpoint
    successfully returns a list of all interaction objects, ensuring that the
    endpoint is correctly fetching data from the data store.
    """
    response = client.get("/interactions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_message():
    """
    Test the creation of a new message within an interaction.

    This test first creates a new interaction and then posts a message to this interaction.
    It verifies that the message creation is successful and the returned message data
    matches the data sent in the request.
    """
    # Create an interaction first
    interaction_response = client.post(
        "/interactions", json={"model_name": "GPT4", "role": "System"}
    )
    interaction_id = interaction_response.json()["id"]

    # Test creating a message
    message_response = client.post(
        f"/interactions/{interaction_id}/messages",
        params={"content": "Hello", "role": "human"},
    )
    print(message_response.json())  # Add this line

    assert message_response.status_code == 200
    message_data = message_response.json()
    assert message_data["content"] == "Hello"
    assert message_data["role"] == "human"
