from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools
from langchain_community.tools import YahooFinanceNewsTool
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_MODEL_NAME = os.getenv('GROQ_MODEL_NAME')

@CrewBase
class StockAnalysisCrew:
	"""Stockanalysis crew"""
	llm = LLM(
		model=GROQ_MODEL_NAME,
		api_key=GROQ_API_KEY,
		base_url="https://api.groq.com/openai/v1"
	)

	@agent
	def research_analyst_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['research_analyst_agent'],
			tools=[
				BrowserTools.scrape_and_summarize_website,
				SearchTools.search_internet,
				CalculatorTools.calculate,
				SECTools.search_10q,
				SECTools.search_10k
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
			BrowserTools.scrape_and_summarize_website,
			SearchTools.search_internet,
			SearchTools.search_news,
			YahooFinanceNewsTool(),
			SECTools.search_10q,
			SECTools.search_10k
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
				BrowserTools.scrape_and_summarize_website,
				SearchTools.search_internet,
				SearchTools.search_news,
				CalculatorTools.calculate,
				YahooFinanceNewsTool()
      		],
			llm=self.llm,
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