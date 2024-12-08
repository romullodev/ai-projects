
from langchain.tools import tool
from LangChain_Projects.SEARCH.search_internet_main import search_and_extract
from LangChain_Projects.SEARCH.search_news_main import search_news_and_extract


class SearchToolsV2():

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet 
        about a a given topic and return relevant results"""
        
        result = search_and_extract(query)
        return result
            
    @tool("Search news on the internet")
    def search_news(query):
        """Useful to search news about a company, stock or any other
        topic and return relevant results"""""
        
        result = search_news_and_extract(query)

        return result
