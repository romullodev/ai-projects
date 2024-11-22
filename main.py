import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import streamlit as st

# Configuração da página (primeira linha)
st.set_page_config(
    page_title="Projetos de IA",
    page_icon=":bar_chart:",
    layout="wide"  # ou "centered"
)

from LangChain_Projects.RAG_PDF.search_page import createRagSearchPage
from LangChain_Projects.LLM_FINANCE.finance_page import createPersonalFinanceDashboard
from CrewAi_Projects.jokes.src.jokes.jokes_page import jokeGenerator
import os

# Variável global para armazenar o modelo selecionado
model_selected = "llama-3.2-90b-vision-preview"

def rag():
    global model_selected
    createRagSearchPage("RAG - Retrieval-Augmented Generation", model_selected)

def finances():
    global model_selected
    createPersonalFinanceDashboard("Dashboard de Finanças Pessoais", model_selected)

def joke():
    global model_selected
    jokeGenerator("Gerador de Piadas", model_selected)    

page_names_to_functions = {
    "Home": None,
    "RAG - Retrieval-Augmented Generation": rag,
    "Dashboard de Finanças Pessoais": finances,
    "Gerador de Piadas": joke,
}

def main():
    global model_selected  # Indica que a variável global deve ser utilizada
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    model_selected = st.selectbox("Selecione o modelo de IA", ["mixtral-8x7b-32768", "llama-3.2-90b-vision-preview", "llama-3.1-70b-versatile"])
    
    page = st.sidebar.selectbox("Navegação", page_names_to_functions.keys())
    os.environ["GROQ_API_KEY"] = st.sidebar.text_input("Insira sua chave da API GROK:")
    st.sidebar.button("Inserir")

    if page == "Home":
        st.title("Página Principal")
        st.write("Escolha uma página para navegar")
    else:
        page_names_to_functions[page]()

if __name__ == "__main__":
    main()