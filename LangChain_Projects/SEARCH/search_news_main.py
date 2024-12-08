import requests
from bs4 import BeautifulSoup

def search_news_and_extract(topic, max_top_results = 4):
    # Faz uma requisição HTTP para o Google News
    url = f"https://www.google.com/search?q={topic}&tbm=nws"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extrai os resultados da busca
    main = soup.select_one('#main')
    results = main.select('div.SoaBEf')
    row = results[5]
    


    resultado = ""
    for row in results[:max_top_results]:    
        title = row.select_one('div.n0jPhd.ynAwRc.MBeuO.nDgy9d')
        link = row.select_one('a')
        description = row.select_one('div.GI74Re.nDgy9d')

        resultado += f"""
            
            title: {title.text if title else None}
            site: {link['href'] if link else None}
            snippet: {description.text if description else None}
        """

    return resultado