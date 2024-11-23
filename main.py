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
    createRagSearchPage("1 - Geração Aumentada por Recuperação (RAG)", model_selected)

def finances():
    global model_selected
    createPersonalFinanceDashboard("2 - Organizador Financeiro", model_selected)

def joke():
    global model_selected
    jokeGenerator("3 - Gerador de Piadas", model_selected)    

page_names_to_functions = {
    "Home": None,
    "1. RAG": rag,
    "2. Organizador Financeiro": finances,
    "3. Gerador de Piadas": joke,
}

import requests

# Função para criar um card para cada página
def create_card(title, subtitle, description, file_path, button_name, file_name, mime):
    st.markdown(f"## {title}")
    st.markdown(f"### {subtitle}")
    st.write(description)
    if file_path:
        key = f"{button_name}{title}"
        with open(file_path, 'rb') as f:
            data = f.read()
        st.download_button(
            key=key,
            label=button_name,
            data=data,
            file_name=file_name,
            mime=mime
        )

def homeDescription():

    # Página principal
    st.title("Página Inicial")
    st.write("Bem-vindo ao guia dos projetos. Abaixo encontram-se informações sobre cada uma das aplicações. Se desejar, insira sua própria chave da API GROQ. Caso não tenha, crie a sua de forma gratuita em https://groq.com/")

    # Card da página 1
    create_card(
        title = "1 - Geração Aumentada por Recuperação (RAG)",
        subtitle = "Arquivos de texto em PDF",
        description = "Utilize o arquivo de exemplo (Constituição Federal, Capítulo 1, Art. 5 ao 7) e realize perguntas sobre o conteúdo do arquivo. Esta aplicação foi desenvolvida pelo framework Langchain.",
        file_path = "LangChain_Projects/RAG_PDF/cf_art1_art5.pdf",
        button_name = "Baixar Constituição Federal",
        file_name = "cf_1988.pdf",
        mime = 'application/pdf'
    )

    # Card da página 2
    create_card(
        title = "2 - Organizador Financeiro",
        subtitle = "Extratos no formato OFX",
        description = "Utilize o arquivo de exemplo no formato OFX para observar a classificação gerada por esta aplicação em Langchain.",
        file_path = "LangChain_Projects/LLM_FINANCE/demo_ofx.ofx",
        button_name= "Baixar Transações Demo - OFX",
        file_name= "demo_ofx.ofx",
        mime= 'application/ofx'
    )

    # Card da página 3
    create_card(
        title = "3 - Gerador de Piadas",
        subtitle = "Escolha um tema",
        description = "Insira um tema qualquer para que a seja gerada  uma piada por agentes inteligentes.  Esta aplicação foi desenvolvida pelo framework CrewAi.",
        file_path = None,  # Se não houver link para download, passe None,
        button_name = None,
        file_name = None,
        mime = None
    )

def main():
    global model_selected  # Indica que a variável global deve ser utilizada
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    model_selected = st.selectbox("Modelos Disponíveis", ["mixtral-8x7b-32768", "llama-3.2-90b-vision-preview", "llama-3.1-70b-versatile"])
    
    page = st.sidebar.selectbox("Navegação", page_names_to_functions.keys())
    groq_key = st.sidebar.text_input("Insira sua Chave da API GROK (Opcional)")
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key
    else:
        os.environ["GROQ_API_KEY"] = "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"
    st.sidebar.button("Inserir")

    if page == "Home":
        homeDescription()    
    else:
        page_names_to_functions[page]()        

if __name__ == "__main__":
    main()