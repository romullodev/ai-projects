import LangChain_Projects.SCRAPING.scraping_main
# from LangChain_Projects.SCRAPING.scraping_main import save_scraping_sites_results

# save_scraping_sites_results([
#     "https://finance.yahoo.com/news/microsoft-corporation-inc-msft-dominating-181949127.html",
#     "https://finance.yahoo.com/news/microsoft-corporation-inc-msft-dominating-181949127.html"
#     ])

from LangChain_Projects.SEARCH.search_internet_main import search_and_extract

topic = "inteligência artificial"
resultados = search_and_extract(topic)
print(resultados)