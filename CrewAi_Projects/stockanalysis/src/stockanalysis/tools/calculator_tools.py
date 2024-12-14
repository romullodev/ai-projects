from crewai.tools import tool
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

@tool("Make a calculation")
def calculate(expression: str):
  """Useful to perform any mathematical calculations, 
  like sum, minus, multiplication, division, etc.
  The input to this tool should be a mathematical 
  expression, a couple examples are `200*7` or `5000/2*10`
  """

  return eval(expression)
