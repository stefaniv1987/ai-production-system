# AI Production System

# AI Production System

Production-ready AI assistant using RAG, LangChain, LangGraph, MCP adapters, observability, Docker, and Kubernetes.

## Objective

This project implements an AI assistant capable of answering user questions using contextual retrieval, orchestration workflows, external tool adapters, and production-ready monitoring practices.

## Architecture

User Question
→ FastAPI Gateway
→ LangGraph Agent
→ RAG Retrieval Service
→ LangChain Response Generation
→ MCP External Tool Adapter
→ Observability Layer

## Main Components

- **Retrieval:** semantic search using embeddings and ChromaDB.
- **Ranking:** prioritizes the most relevant retrieved documents.
- **Orchestration:** LangChain coordinates prompts, context, and LLM calls.
- **Agent:** LangGraph manages iterative reasoning cycles.
- **MCP Adapters:** controlled and secure integration with external tools such as Jira.
- **Observability:** tracks latency, token usage, errors, and system behavior.
- **Deployment:** Docker and Kubernetes configuration for scalable deployment.

## Technologies

- Python
- FastAPI
- LangChain
- LangGraph
- ChromaDB
- OpenAI
- Docker
- Kubernetes
- LangSmith / Arize AI

## How to Run

```bash
docker-compose up --build
