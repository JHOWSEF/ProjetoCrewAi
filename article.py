from pydantic import BaseModel, Field
class Article(BaseModel):
    title: str = Field(description="Título do artigo")
    content: str = Field(description="Conteúdo do artigo")
    key_words: list = Field(description="Palavras-chave do conteúdo do artigo")