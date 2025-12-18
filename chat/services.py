# chat/services.py
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

def summarizer_agent(message):
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0.2
    )

    prompt = PromptTemplate(
        input_variables=["query"],
        template="Summarize the following user query in one sentence:\n{query}"
    )

    chain = prompt | llm
    return chain.invoke({"query": message}).content

def answer_agent(message):
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.4
    )

    prompt = PromptTemplate(
        input_variables=["query"],
        template="Answer the following question clearly:\n{query}"
    )

    chain = prompt | llm
    return chain.invoke({"query": message}).content

