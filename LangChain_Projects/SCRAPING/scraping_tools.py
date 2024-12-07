from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

def get_page_content(sites: list[str]): 
    # Carregar a página e transformar o HTML
    loader = AsyncChromiumLoader(sites)
    html = loader.load()    
    bs_transformer = BeautifulSoupTransformer()
    docs = bs_transformer.transform_documents(
        documents=html, 
        unwanted_tags=("script", "style"),         
        tags_to_extract = ("p", "div"),
        )

    result = []
    for doc in docs:
        result.append(doc.page_content)        
    return result