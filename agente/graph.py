from typing import TypedDict

from langgraph.graph import StateGraph, END

from retrieval.rag import search_documents
from orquestacion.chain import generate_response


class AgentState(TypedDict):
    question: str
    context: str
    answer: str
    is_answer_sufficient: bool


def retrieve_context(state: AgentState) -> AgentState:
    """
    Retrieves relevant documents using the RAG service.
    """
    docs = search_documents(state["question"])

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    state["context"] = context
    return state


def generate_answer(state: AgentState) -> AgentState:
    """
    Generates an answer using the retrieved context and the user's question.
    """
    answer = generate_response(
        context=state["context"],
        question=state["question"]
    )

    state["answer"] = answer
    return state


def evaluate_answer(state: AgentState) -> str:
    """
    Simple evaluation step.
    In a production system, this could use an LLM judge or retrieval score.
    """
    answer = state.get("answer", "")

    if len(answer.strip()) > 50:
        return "sufficient"

    return "insufficient"


def ask_for_more_context(state: AgentState) -> AgentState:
    """
    Placeholder for iterative reasoning.
    In a real implementation, this node could reformulate the query
    and search for more context.
    """
    state["question"] = state["question"] + " Please provide more detailed context."
    return state


graph = StateGraph(AgentState)

graph.add_node("retrieve_context", retrieve_context)
graph.add_node("generate_answer", generate_answer)
graph.add_node("ask_for_more_context", ask_for_more_context)

graph.set_entry_point("retrieve_context")

graph.add_edge("retrieve_context", "generate_answer")

graph.add_conditional_edges(
    "generate_answer",
    evaluate_answer,
    {
        "sufficient": END,
        "insufficient": "ask_for_more_context"
    }
)

graph.add_edge("ask_for_more_context", "retrieve_context")

agent = graph.compile()


def run_agent(question: str):
    """
    Runs the LangGraph agent.
    """
    initial_state = {
        "question": question,
        "context": "",
        "answer": "",
        "is_answer_sufficient": False
    }

    result = agent.invoke(initial_state)

    return result["answer"]
