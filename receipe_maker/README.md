# Recipe Assistant API

This project provides a recipe generation API using Groq's LLM and FastAPI. It allows users to get detailed recipes based on their questions or ingredient lists.

## Project Structure

- `llm.py`: Contains the core recipe generation logic using Groq's LLM
- `main.py`: FastAPI application that exposes the recipe generation as a REST API
- `requirements.txt`: Project dependencies

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you have a valid Groq API key. The current implementation uses a hardcoded key, but for production use, you should use environment variables.

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Welcome Message
- **Endpoint**: `GET /`
- **Response**: Welcome message with usage instructions
- **Example**:
```bash
curl http://localhost:8000/
```

### 2. Generate Recipe
- **Endpoint**: `POST /recipe`
- **Request Body**:
```json
{
    "question": "How to make pasta with tomatoes?"
}
```
- **Response**:
```json
{
    "recipe": "Detailed recipe instructions..."
}
```
- **Example**:
```bash
curl -X POST "http://localhost:8000/recipe" \
     -H "Content-Type: application/json" \
     -d '{"question": "How to make pasta with tomatoes?"}'
```

## Interactive Documentation

FastAPI provides automatic interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Dependencies

- `groq`: For LLM integration
- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `pydantic`: Data validation
- `python-multipart`: Form data handling

## Security Note

The current implementation includes a hardcoded API key. For production use:
1. Move the API key to environment variables
2. Implement proper authentication
3. Add rate limiting
4. Use HTTPS

## Error Handling

The API includes basic error handling for:
- Invalid requests
- API errors
- LLM generation errors

All errors return appropriate HTTP status codes and error messages. 