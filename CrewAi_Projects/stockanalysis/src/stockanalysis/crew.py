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
class StockAnalysisCrew:
	"""Stockanalysis crew"""
	llm2 = LLM(
		model="llama-3.1-8b-instant", 
		api_key=GROQ_API_KEY,
		temperature=0.0,
		base_url="https://api.groq.com/openai/v1"
	)
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

	@agent
	def financial_analyst_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['financial_analyst_agent'],
			verbose=True,
			tools=[
			scrape_and_summarize_website,
			search_internet,
			search_news,	
			search_10q,
			search_10k,
			search_news_on_yahoo,
      		],
			llm=self.llm,
			max_iter=30
		)
	
	@agent
	def investment_advisor_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['investment_advisor_agent'],
			verbose=True,
			tools=[
				scrape_and_summarize_website,
				search_internet,
				search_news,
				calculate,
				search_news_on_yahoo
      		],
			llm=self.llm2,
			max_iter=30
		)


	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def financial_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['financial_analysis_task'],
		)
	
	@task
	def filings_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['filings_analysis_task'],
		)
	
	@task
	def recommend_task(self) -> Task:
		return Task(
			config=self.tasks_config['recommend_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Stockanalysis crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)