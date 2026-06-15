# Architecture

The AI Production System follows a modular microservices-oriented architecture.

## General Flow

1. The user submits a question through the FastAPI endpoint.
2. The LangGraph agent receives the question.
3. The RAG service retrieves relevant context from the vector database.
4. LangChain generates a response using the retrieved context.
5. MCP adapters allow controlled access to external tools.
6. Observability modules collect metrics and logs.

## Architecture Diagram

User
→ FastAPI Gateway
→ LangGraph Agent
→ RAG Service
→ Vector Database
→ LangChain LLM Chain
→ Response

## Key Design Decisions

- RAG is used to reduce hallucinations through contextual grounding.
- LangChain is used for orchestration and prompt management.
- LangGraph enables iterative reasoning and decision-based flows.
- MCP adapters isolate access to external systems.
- Docker and Kubernetes support portability and scalability.
