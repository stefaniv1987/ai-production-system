# Architectural Decisions

## RAG

Retrieval-Augmented Generation was selected to improve answer accuracy by grounding responses in retrieved documents.

## LangChain

LangChain was selected because it provides reusable chains, prompt templates, model integrations, and retrieval workflows.

## LangGraph

LangGraph was selected to model agentic workflows with state, nodes, edges, and iterative decision cycles.

## MCP Adapters

External tools are accessed through MCP-style adapters to improve security, permissions control, and traceability.

## Observability

Observability was included to monitor latency, errors, token usage, and quality metrics.

## Deployment

Docker and Kubernetes were selected to support reproducible local execution and scalable production deployment.
