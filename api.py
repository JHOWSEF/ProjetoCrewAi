from fastapi import FastAPI
from pydantic import BaseModel
from agents import ResearcherAgent, WriterAgent

app = FastAPI()

class ArticleRequest(BaseModel):
    topic: str

@app.post("/generate_article/")
async def generate_article(request: ArticleRequest):
    # Criando os agentes
    fetcher_agent = ResearcherAgent()
    generator_agent = WriterAgent()
    
    # Buscando conteúdo e gerando o artigo
    content = fetcher_agent.run(request.topic)
    article = generator_agent.run(content)
    
    return {"article": article}

