# FastAPI AI Chat Application

## Description

This FastAPI AI chat application is a RESTful API service that enables users to have AI-powered chat interactions. It uses FastAPI framework and integrates AI capabilities for a sophisticated human-machine interaction experience. The application is designed to be simple, scalable, and ready for production deployment.

## Features

- Create new AI chat interactions.
- Retrieve all interactions.
- Add messages to interactions.
- Fetch all messages within an interaction.
- Mock AI responses using `gpt4free`.

## Installation

### Prerequisites

- Python 3.11
- Docker (for containerization)
- Docker Compose (for easy local deployment)

### Setup

1. Clone the repository:
   ```bash
   git clone [repository_url]
   ```

2. Navigate to the project directory:
   ```bash
   cd fastapi-ai-chat-app
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Using Docker Compose

1. Build and run the application:
   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://localhost:8000`.

### Locally (without Docker)

1. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the application at `http://127.0.0.1:8000`.

## Usage

### API Endpoints

- `POST /interactions`: Create a new interaction.
- `GET /interactions`: Fetch all interactions.
- `POST /interactions/{id}/messages`: Add a message to an interaction.
- `GET /interactions/{id}/messages`: Fetch all messages within an interaction.

## Testing

Run the tests with:

```bash
pytest
```