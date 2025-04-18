from crewai import Agent
from wikipedia_tool import WikipediaTool
from gemini_llms import create_gemini_llm



class ResearcherAgent:
    def create(self):
        llm = create_gemini_llm()
        wiki = WikipediaTool()
        return Agent(
            role="Pesquisador experiente sobre todos assuntos!",
            goal="Buscar informações relevantes na Wikipedia",
            backstory="Especialista em coletar informações precisas e rápidas.",
            tools=[wiki],
            verbose=True,
            llm=llm,
            allow_delegation=False
        )
class WriterAgent:
    def create(self):
        llm = create_gemini_llm()
        return Agent(
            role="Escritor de artigos com muita maestria!",
            goal="Escrever artigos de no mínimo 300 palavras baseados em pesquisa.",
            backstory="Você é um escritor com muitos anos de experiência\n"
                "Você utiliza as informaçoes coletadas pelo Pesquisador para escrever sobre {topic}\n"
                "Seus textos são cativantes, e buscam informar e entreter o leitor, "
                "leve em consideração que o leitor pode não possuir conhecimentos aprofundados sobre {topic}"
                "Você tem um conhecimento vasto sobre às normas da língua portuguesa "
                "e não costuma cometer erros ortográgicos, gramaticais ou de sinais\n"
                "O Seu texto não deve possuir tags de html\n "
                "Por fim, envie o seu texto para o Revisor sênior\n"
                "Você deve se comunicar somente através da língua portuguesa",
            verbose=True,
            llm=llm,
            allow_delegation=False
        )