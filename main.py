import streamlit as st
import streamlit as st

# Configuração da página (primeira linha)
st.set_page_config(
    page_title="Projetos de IA",
    page_icon=":bar_chart:",
    layout="wide"  # ou "centered"
)

from LangChain_Projects.RAG_PDF.search_page import createRagSearchPage
from LangChain_Projects.LLM_FINANCE.dash import createPersonalFinancesDashboard
from CrewAi_Projects.jokes.src.jokes.jokes_page import jokeGenerator

def rag():
    createRagSearchPage("Regimento Interno - Plaza Tambiá")

def finances():
    createPersonalFinancesDashboard("Dashboard de Finanças Pessoais")

def joke():
    jokeGenerator("Gerador de Piadas")    

page_names_to_functions = {
    "Home": None,
    "Regimento Interno - Plaza Tambiá": rag,
    "Dashboard de Finanças Pessoais": finances,
    "Gerador de Piadas": joke,
}

def main():
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    page = st.sidebar.selectbox("Navegação", page_names_to_functions.keys())

    if page == "Home":
        st.title("Página Principal")
        st.write("Escolha uma página para navegar")
    else:
        page_names_to_functions[page]()

if __name__ == "__main__":
    main()