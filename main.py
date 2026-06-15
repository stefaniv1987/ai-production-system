from fastapi import FastAPI
from pydantic import BaseModel

from agente.graph import run_agent


app = FastAPI(
    title="AI Production System",
    description="Production-ready AI assistant using RAG, LangChain, LangGraph, MCP, and observability.",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "AI Production System is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = run_agent(request.question)

    return {
        "question": request.question,
        "answer": answer
    }
