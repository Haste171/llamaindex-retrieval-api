from fastapi import APIRouter
from pydantic import BaseModel
from routers.utils.engine import Engine

query_engine = Engine()
router = APIRouter()

class QueryInput(BaseModel):
    prompt: str
    namespace: str
    temperature: float = 0.0

@router.post("/query")
async def query(input: QueryInput):
    response = query_engine.query(input.prompt, input.namespace, input.temperature)
    return {
        "input": input.prompt,
        "response": response
    }