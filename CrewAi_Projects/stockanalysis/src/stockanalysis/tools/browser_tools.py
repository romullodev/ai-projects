from crewai.tools import tool
from LangChain_Projects.SCRAPING.scraping_main import scraping_single_website
from crewai.tools import BaseTool
from langchain_community.tools import YahooFinanceNewsTool


@tool("Scrape website content")
def scrape_and_summarize_website(website: str) -> str:
  """
  Useful to scrape and summarize a website content.
  provide a string as input with your website to be scraped.
  For example: `https://www.example.com`
  """
  result = scraping_single_website(website)
  return result


@tool("search on yahoo")
def search_news_on_yahoo(ticker: str) -> str:
  """
  Useful for when you need to find financial news
  about a public company.Input should be a company ticker.
  For example, AAPL for Apple, MSFT for Microsoft.
  """
  
  yahoo = YahooFinanceNewsTool()  
  result = yahoo.run(tool_input=ticker)
  return result
    
