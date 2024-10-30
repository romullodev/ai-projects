from crewai import Agent, Crew, Process, Task, LLM
from tools.search_tools import SearchTools
from tools.browser_tools import BrowserTools
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

@CrewBase
class JokesCrew:
	"""Jokes crew"""
	llm = LLM(
		model="mixtral-8x7b-32768",  # or another Groq model
		api_key=GROQ_API_KEY,
		base_url="https://api.groq.com/openai/v1"
	)


	@agent
	def joke_generator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['joke_generator_agent'],
			verbose=True,
			llm=self.llm
		)

	@agent
	def joke_picker_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['joke_picker_agent'],
			verbose=True,
			llm=self.llm
		)
	
	@task
	def generate_joke_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_joke_task'],
		)

	@task
	def pick_joke_task(self) -> Task:
		return Task(
			config=self.tasks_config['pick_joke_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Jokes crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)