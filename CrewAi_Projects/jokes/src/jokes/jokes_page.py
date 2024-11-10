import streamlit as st
from CrewAi_Projects.jokes.src.jokes.make_joke import createJoke

def jokeGenerator(title: str, selected_model: str):
    # Título da página
    st.title(title)

    # Campo de texto para a entrada do usuário
    topic = st.text_input("Digite um tópico para a piada:")

    # Botão para iniciar a pesquisa
    if st.button("Criar"):
        if topic:
            result = createJoke(topic, selected_model)
            st.text_area("Resultado:", value=result, height=200)
        else:
            st.warning("Por favor, digite um tópico.")