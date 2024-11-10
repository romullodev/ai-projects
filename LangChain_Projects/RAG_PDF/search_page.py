import streamlit as st
from LangChain_Projects.RAG_PDF.rag import search
from LangChain_Projects.RAG_PDF.generate_db import createDb
from LangChain_Projects.RAG_PDF.generate_db import get_db_retriever
from LangChain_Projects.RAG_PDF.generate_db import saveFile
from langchain.document_loaders import PyPDFLoader

# Variável global
retriever_chain = None

def createRagSearchPage(title: str, selected_model: str):
    global retriever_chain  # Indica que a variável global deve ser utilizada
    # Título da página
    st.title(title)

    # Upload de PDF
    uploaded_file = st.file_uploader("Carregar um PDF", type="pdf")

    if uploaded_file is None:
        retriever_chain = None
    
    if uploaded_file is not None:
        if retriever_chain is None:
            saveFile(uploaded_file)
            createDb()
            retriever_chain = get_db_retriever()
        
    if retriever_chain is not None:
        # Campo de texto para a entrada do usuário
        query = st.text_input("Digite sua pergunta:")

        # Botão para iniciar a pesquisa
        if st.button("Pesquisar"):
            if query:
                result = search(query, selected_model, retriever_chain)
                st.text_area("Resultado:", value=result, height=200)
            else:
                st.warning("Por favor, digite uma pergunta.")
                        