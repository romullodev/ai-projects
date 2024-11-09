#from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from transformers import AutoTokenizer, AutoModel

pdf_file = "LangChain_Projects/RAG_PDF/regimento_plaza.pdf"
index_file = "regimento_plaza"
model_name = "sentence-transformers/all-mpnet-base-v2"

"""
Cria um banco de dados vetorial a partir de um PDF utilizando o FAISS e a Langchain.

Args:
    pdf_file (str): Caminho para o arquivo PDF.
    index_file (str): Caminho para salvar o índice do FAISS.
    model_name (str, optional): Nome do modelo Hugging Face a ser utilizado. Defaults to "sentence-transformers/all-mpnet-base-v2".
"""

# Carregar o PDF e criar documentos
loader = PyPDFLoader(pdf_file)
documents = loader.load()

# Carregar o modelo Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Criar embeddings
embeddings = HuggingFaceEmbeddings(model_name=model_name)
text_embeddings = embeddings.embed_documents([doc.page_content for doc in documents])

# Criar o índice FAISS
#vectorstore = FAISS.from_embeddings(text_embeddings=text_embeddings, embedding=embeddings)
vectorstore = FAISS.from_documents(documents=documents, embedding=embeddings)

# Salvar o índice
vectorstore.save_local(index_file)

def get_db_retriever():

    # Carregar o índice
    vectorstore = FAISS.load_local(index_file, embeddings, allow_dangerous_deserialization=True)
    return vectorstore.as_retriever()