from CrewAi_Projects.stockanalysis.src.stockanalysis.tools.browser_tools import scrape_and_summarize_website, search_news_on_yahoo
from CrewAi_Projects.stockanalysis.src.stockanalysis.tools.calculator_tools import calculate
from CrewAi_Projects.stockanalysis.src.stockanalysis.tools.search_tools import search_internet,search_news
from CrewAi_Projects.stockanalysis.src.stockanalysis.tools.sec_tools import search_10k, search_10q
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


import os
from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

@CrewBase
class GenerateResearchReportCrew:
	"""Research Report Crew"""
	llm = LLM(
		model="llama-3.3-70b-versatile",
		api_key=GROQ_API_KEY,
		base_url="https://api.groq.com/openai/v1"
	)

	@agent
	def research_analyst_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['research_analyst_agent'],
			tools=[
				scrape_and_summarize_website,
				search_internet,
				calculate,
				search_10q,
				search_news_on_yahoo,
			],
			verbose=True,
			max_iter=30,
			llm=self.llm
		)


	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Stockanalysis crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)