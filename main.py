from fastapi import FastAPI
from crew import ArticleCrew
from article import Article
from fastapi.responses import HTMLResponse



app = FastAPI()

@app.get("/generate-article/", response_model=Article)
def generate_article(topic: str):
    crew = ArticleCrew().create()
    result = crew.kickoff(inputs={"topic": topic})
    

    content = result.output if hasattr(result, "output") else str(result)
    fake_keywords = topic.split()  # só como placeholder

    article = Article(
        title=topic,
        content=content,
        key_words=fake_keywords
    )
    return article

@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html", encoding="utf-8").read()