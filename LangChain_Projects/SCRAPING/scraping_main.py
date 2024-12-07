from langchain_core.prompts import PromptTemplate
from LangChain_Projects.SCRAPING.scraping_tools import get_page_content
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv

def save_scraping_sites_results(sites: list[str]):
    results = scraping_multiples_sites(sites)
    #page_content_save_path = "LangChain_Projects/SCRAPING/page_content_"
    summarized_content_save_path = "LangChain_Projects/SCRAPING/summarized_content_"
    
    for i, summary in enumerate(results):    
        save_path = summarized_content_save_path + str(i) + ".txt"
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(summary)

def scraping_multiples_sites(websites: list[str]):

    template = """
    You're a Principal Researcher at a big company and you need to do a research about a given topic. 
    Your duty is do an amazing research and summaries based on the content you are working with.

    Now, you have to analyze and summarize the content below. Make sure to include the most relevant information 
    in the summary, return only the summary nothing else.

    CONTENT

    {text}
    """

    prompt = PromptTemplate.from_template(template=template)

    _ = load_dotenv(find_dotenv())

    model = "llama-3.1-8b-instant"
    llm = ChatGroq(model=model, temperature=0.0)
    chain = prompt | llm
    page_contents = get_page_content(websites)

    
    results = []
    for content in page_contents:                
        summary = chain.invoke(content).content
        results.append(summary)        
    return results        

def scraping_single_website(website: str):
    result = scraping_multiples_sites([website])
    return result[0]


        