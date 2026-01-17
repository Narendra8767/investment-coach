
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.guardrails import is_restricted
from app.prompts import COACH_PROMPT, MARKET_PROMPT, REFUSAL
from app.sessions import get_vectorstores
from app.rag import retrieve_from_vectorstores
from app.sessions import get_vectorstores
from app.news import fetch_market_news
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# -------- LLM --------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# -------- Prompts --------
coach_prompt = ChatPromptTemplate.from_template(COACH_PROMPT)
market_prompt = ChatPromptTemplate.from_template(MARKET_PROMPT)

# -------- Runnable Chains --------
coach_chain = (
    coach_prompt
    | llm.with_config({"run_name": "Coach LLM"})
)

market_chain = (
    market_prompt
    | llm.with_config({"run_name": "Market LLM"})
)



# -------- Intent Classifier --------
def classify_intent(message: str) -> str:
    msg = message.lower()

    if is_restricted(msg):
        return "restricted"
    if "market" in msg or "today" in msg or "news" in msg:
        return "market"
    return "coach"


def run_chat(message: str, session_id: str) -> str:
    intent = classify_intent(message)

    if intent == "restricted":
        return REFUSAL

    if intent == "market":
        try:
            news_context = fetch_market_news()
        except Exception as e:
            news_context = "Market news is temporarily unavailable."

        enriched_question = f"""
User question:
{message}

Latest market news:
{news_context}
"""

        response = market_chain.invoke(
            {"question": enriched_question}
        )
        return response.content

    # ---- Coach with PDF RAG ----
    vectorstores = get_vectorstores(session_id)
    context = retrieve_from_vectorstores(message, vectorstores)

    prompt_input = message
    if context:
        prompt_input += "\n\nUser uploaded documents:\n" + context

    response = coach_chain.invoke({"question": prompt_input})
    return response.content
