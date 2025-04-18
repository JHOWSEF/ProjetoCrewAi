from crewai import Crew, Task
from agents import ResearcherAgent, WriterAgent

class ArticleCrew:
    def __init__(self):
        self.researcher = ResearcherAgent().create()
        self.writer = WriterAgent().create()

    def create(self):
        research_task = Task(
            description="Pesquise no Wikipedia sobre {topic} e entregue um resumo claro e completo.",
            expected_output="Resumo da Wikipedia sobre o tema {topic}.",
            agent=self.researcher
        )

        writing_task = Task(
            description="Com base no resumo da pesquisa sobre {topic}, escreva um artigo detalhado e envolvente com no mínimo 300 palavras.",
            expected_output="Artigo de no mínimo 300 palavras sobre {topic}.",
            agent=self.writer
        )

        crew = Crew(
            agents=[self.researcher, self.writer],
            tasks=[research_task, writing_task],
            verbose=True
        )
        return crew

