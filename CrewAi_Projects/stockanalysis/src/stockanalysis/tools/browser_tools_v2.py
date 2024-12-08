from json import tool
from LangChain_Projects.SCRAPING.scraping_main import scraping_single_website


class BrowserToolsV2():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""    
    result = scraping_single_website(website)
    return result
    
