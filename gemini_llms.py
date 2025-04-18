import os
from crewai import LLM

def create_gemini_llm():
    # Defina a API KEY no ambiente
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBL1UxVwfy-j3i1Li4BnUC1lHsKVfLrG80"  # ou configure via dotenv

    # Retorna o LLM compatível com CrewAI e LiteLLM
    return LLM(
        model="gemini/gemini-2.0-flash",  # Pode ser gemini-1.5-pro se você tiver acesso
        api_key=os.environ["GOOGLE_API_KEY"]
    )
