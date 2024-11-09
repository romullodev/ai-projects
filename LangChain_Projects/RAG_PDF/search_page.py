import streamlit as st
from LangChain_Projects.RAG_PDF.rag import search

def createRagSearchPage(title: str):
    # Título da página
    st.title(title)

    # Campo de texto para a entrada do usuário
    query = st.text_input("Digite sua pergunta:")

    # Botão para iniciar a pesquisa
    if st.button("Pesquisar"):
        if query:
            result = search(query)
            st.text_area("Resultado:", value=result, height=200)
        else:
            st.warning("Por favor, digite uma pergunta.")