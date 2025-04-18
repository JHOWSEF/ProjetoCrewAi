from crewai.tools import BaseTool
import requests
from pydantic import Field

class WikipediaTool(BaseTool):
    base_url: str = Field("https://pt.wikipedia.org/w/api.php", description="Base URL for Wikipedia API")
    name: str = "Wikipedia Search Tool"  # Adicionando o campo 'name'
    description: str = "Busca informações resumidas da Wikipedia sobre um tópico específico."  # Adicionando o campo 'description'

    def _run(self, topic: str) -> str:
        params = {
            "action": "query",
            "prop": "extracts",
            "exlimit": 1,
            "explaintext": 1,
            "titles": topic,
            "format": "json",
            "utf8": 1,
            "redirects": 1
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))
        return page.get("extract", "Nenhuma informação encontrada.")

# Instanciando o WikipediaTool e passando as informações corretamente
wikipedia_tool = WikipediaTool(name="Wikipedia Search Tool", description="Busca informações resumidas da Wikipedia sobre um tópico específico.")
