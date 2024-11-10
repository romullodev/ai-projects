import streamlit as st
import pandas as pd
import plotly.express as px
from LangChain_Projects.LLM_FINANCE.generate_finance import deleteAllFilesFrom, saveFile, generateCsvFile

# Filtered Data Frame
data_frame = None
uploaded_file = None

def createPersonalFinanceDashboard(title: str, selcted_model: str):
    global data_frame
    global uploaded_file
    
    # Título do Dashboard
    st.title(title)

    # Upload de OFX
    uploaded_file = st.file_uploader("Carregar um extrato OFX", type="ofx")

    if uploaded_file is None:
        data_frame = None
    if uploaded_file is not None:
        if data_frame is None:
            deleteAllFilesFrom("LangChain_Projects/LLM_FINANCE/extratos")
            saveFile(uploaded_file)
            generateCsvFile(selcted_model)
            data_frame = pd.read_csv("LangChain_Projects/LLM_FINANCE/finance.csv")
        
    if data_frame is not None: 
        data_frame["Mês"] = data_frame["Data"]
        data_frame["Data"] = pd.to_datetime(data_frame["Data"])
        data_frame["Data"] = data_frame["Data"].apply(lambda x: x.date())
        data_frame = data_frame[data_frame["Valor"] >= 0]

        def filter_data(df, mes, selected_categories):
            df_filtered = df[df['Mês'] == mes]
            if selected_categories:
                df_filtered = df_filtered[df_filtered['Categorias'].isin(selected_categories)]
            return df_filtered

        # Filtros de data
        st.sidebar.header("Filtros")

        # Definir intervalo de data
        mes = st.sidebar.selectbox("Mês", data_frame["Mês"].unique())


        # Filtro de categoria
        categories = data_frame["Categorias"].unique().tolist()
        selected_categories = st.sidebar.multiselect("Filtrar por Categorias", categories, default=categories)

        df_filtered = filter_data(data_frame, mes, selected_categories)


        # ====================
        c1, c2 = st.columns([0.6, 0.4])

        # c1.subheader("Tabela de Finanças Filtradas")
        c1.dataframe(df_filtered)
        

        # c2.subheader("Distribuição de Categorias")
        category_distribution = df_filtered.groupby("Categorias")["Valor"].sum().reset_index()
        fig = px.pie(category_distribution, values='Valor', names='Categorias', 
                    title='Distribuição por Categoria', hole=0.3
                        )
        c2.plotly_chart(fig, use_container_width=True)