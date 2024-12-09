
from crewai.tools import tool
from LangChain_Projects.SEARCH.search_internet_main import search_and_extract
from LangChain_Projects.SEARCH.search_news_main import search_news_and_extract

@tool("Search the internet")
def search_internet(topic: str) -> str:
    """Useful to search the internet 
    about a a given topic and return relevant results.
    provide a string as input with your topic to be searched.
    For example: `latest new about MSFT`
    """
    
    result = search_and_extract(topic)
    return result
        
@tool("Search news on the internet")
def search_news(topic: str) -> str:
    """Useful to search news about a company, stock or any other
    topic and return relevant results.
    provide a string as input with your topic to be searched.
    For example: `latest new about MSFT` 
    """
    
    result = search_news_and_extract(topic)

    return result
