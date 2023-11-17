from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_interaction():
    response = client.post("/interactions", json={"model_name": "GPT4", "role": "System"})
    assert response.status_code == 200
    data = response.json()
    assert data["settings"]["model_name"] == "GPT4"
    assert "id" in data

def test_get_all_interactions():
    response = client.get("/interactions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_message():
    # Create an interaction first
    interaction_response = client.post("/interactions", json={"model_name": "GPT4", "role": "System"})
    interaction_id = interaction_response.json()["id"]

    # Test creating a message
    message_response = client.post(f"/interactions/{interaction_id}/messages", params={"content": "Hello", "role": "human"})
    print(message_response.json())  # Add this line

    assert message_response.status_code == 200
    message_data = message_response.json()
    assert message_data["content"] == "Hello"
    assert message_data["role"] == "human"
