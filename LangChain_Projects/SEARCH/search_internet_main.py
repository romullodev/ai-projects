from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import requests
from bs4 import BeautifulSoup


def search_and_extract(topic, max_top_results = 4):
    # Busca no Google
    url = f"https://www.google.com/search?q={topic}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extrai os resultados da busca
    main = soup.select_one('#main')
    results = main.select('div.N54PNb.BToiNc')

    resultado = ""
    for row in results[:max_top_results]:    
        title = row.select_one('h3')
        link = row.select_one('a')
        description = row.select_one('div.VwiC3b.yXK7lf.lVm3ye.r025kc.hJNv6b.Hdw6tb')

        resultado += f"""
            
            title: {title.text if title else None}
            site: {link['href'] if link else None}
            snippet: {description.text if description else None}
        """

    return resultado
    
    # formatted_results = []
    
    # for row in results[:max_top_results]:    
    #     title = row.select_one('h3')
    #     link = row.select_one('a')
    #     description = row.select_one('div.VwiC3b.yXK7lf.lVm3ye.r025kc.hJNv6b.Hdw6tb')

    #     formatted_results.append({
    #         "title": title.text if title else None,
    #         "site": link['href'] if link else None,
    #         "snippet": description.text if description else None
    #     })

    # return formatted_results




