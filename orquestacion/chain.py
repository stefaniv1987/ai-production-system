from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
You are an AI assistant.

Use the following context to answer the user's question.

Context:
{context}

Question:
{question}
""")

def generate_response(context: str, question: str):
    chain = prompt | llm
    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content
