import os
import requests
from crewai.tools import tool
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from sec_api import QueryApi
from unstructured.partition.html import partition_html
from dotenv import load_dotenv

load_dotenv()

SEC_API_API_KEY = os.getenv('SEC_API_API_KEY')

@tool("Search 10-Q form")
def search_10q(data: str):
  """
  Useful to search information from the latest 10-Q form for a
  given stock.
  The input to this tool should be a pipe (|) separated text of
  length two, representing the stock ticker you are interested and what
  question you have from it.
  For example, `AAPL|what was last quarter's revenue`.
  """
  stock, ask = data.split("|")
  queryApi = QueryApi(api_key=SEC_API_API_KEY)
  query = {
    "query": f"ticker:{stock} AND formType:\"10-Q\"",
    "from": "0",
    "size": "1",
    "sort": [{ "filedAt": { "order": "desc" }}]
  }
  fillings = queryApi.get_filings(query)['filings']
  if len(fillings) == 0:
    return "Sorry, I couldn't find any filling for this stock, check if the ticker is correct."
  link = fillings[0]['linkToFilingDetails']
  answer = __embedding_search(link, ask)
  return answer

@tool("Search 10-K form")
def search_10k(data: str):
  """
  Useful to search information from the latest 10-K form for a
  given stock.
  The input to this tool should be a pipe (|) separated text of
  length two, representing the stock ticker you are interested and what
  question you have from it.
  For example, `AAPL|what was last quarter's revenue`.
  """
  stock, ask = data.split("|")
  queryApi = QueryApi(api_key=SEC_API_API_KEY)
  query = {
    "query": f"ticker:{stock} AND formType:\"10-K\"",
    "from": "0",
    "size": "1",
    "sort": [{ "filedAt": { "order": "desc" }}]
  }

  fillings = queryApi.get_filings(query)['filings']
  if len(fillings) == 0:
    return "Sorry, I couldn't find any filling for this stock, check if the ticker is correct."
  link = fillings[0]['linkToFilingDetails']
  answer = __embedding_search(link, ask)
  return answer

def __embedding_search(url, ask):
  text = __download_form_html(url)
  elements = partition_html(text=text)
  content = "\n".join([str(el) for el in elements])
  text_splitter = CharacterTextSplitter(
      separator = "\n",
      chunk_size = 1000,
      chunk_overlap  = 150,
      length_function = len,
      is_separator_regex = False,
  )
  docs = text_splitter.create_documents([content])
  retriever = FAISS.from_documents(
    docs, HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
  ).as_retriever()
  answers = retriever.get_relevant_documents(ask, top_k=4)
  answers = "\n\n".join([a.page_content for a in answers])
  return answers

def __download_form_html(url):
  headers = {
    'User-Agent':'Dummy Company anna.sassin@dummy.com',
    'Accept-Encoding':'gzip, deflate',
    'Host':'www.sec.gov'
    }

  response = requests.get(url, headers=headers)
  return response.text
