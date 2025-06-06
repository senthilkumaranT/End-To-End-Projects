from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm import get_recipe

app = FastAPI(title="Recipe API")

class RecipeRequest(BaseModel):
    question: str

@app.post("/recipe")
async def create_recipe(request: RecipeRequest):
    try:
        recipe = get_recipe(request.question)
        return {"recipe": recipe}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to Recipe API. Use POST /recipe endpoint with a question to get recipes."} 