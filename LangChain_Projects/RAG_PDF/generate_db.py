#from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader

save_path = "LangChain_Projects/RAG_PDF/rag_document.pdf"
index_file = "LangChain_Projects/RAG_PDF/index_file"
model_name = "sentence-transformers/all-mpnet-base-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)

def saveFile(uploaded_file):
    # Salva o arquivo, sobrescrevendo se já existir
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

def createDb():
    # Carregar o PDF e criar documentos
    loader = PyPDFLoader(save_path)
    documents = loader.load()

    # Criar o índice FAISS
    vectorstore = FAISS.from_documents(documents=documents, embedding=embeddings)

    # Salvar o índice
    vectorstore.save_local(index_file)

def get_db_retriever():
    # Carregar o índice
    vectorstore = FAISS.load_local(index_file, embeddings, allow_dangerous_deserialization=True)
    return vectorstore.as_retriever()