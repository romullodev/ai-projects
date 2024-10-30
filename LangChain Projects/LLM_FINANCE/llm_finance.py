import ofxparse 
import pandas as pd
import os
from datetime import datetime

df = pd.DataFrame()

for extrato in os.listdir("extratos"): 
    with open(f'extratos/{extrato}', encoding='ISO-8859-1') as ofx_file:
        ofx = ofxparse.OfxParser.parse(ofx_file)
    
    transaction_data = []
    for account in ofx.accounts: 
        for transaction in account.statement.transactions: 
            transaction_data.append({
                "Data": transaction.date,
                "Valor": transaction.amount,
                "Descrição": transaction.memo,
                "ID": transaction.id,
            })

df_temp = pd.DataFrame(transaction_data)
df_temp["Valor"] = df_temp["Valor"].astype(float)
df_temp["Data"] = df_temp["Data"].apply(lambda x: x.date())
df = pd.concat([df, df_temp])

# ========================================
# LLM
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

template = """
Você é um analista de dados, trabalhando em um projeto de limpeza de dados.
Seu trabalho é escolher uma categoria adequada para cada lançamento financeiro
que vou te enviar.

Todos são transações financeiras de uma pessoa física.

Escolha uma dentre as seguintes categorias:
- Alimentação
- Receitas
- Saúde
- Mercado
- Educação
- Compras
- Transporte
- Investimento
- Transferências para terceiros
- Telefone
- Moradia

Escola a categoria deste item:
{text}

Responda apenas com a categoria.
"""

prompt = PromptTemplate.from_template(template=template)
#chat = ChatGroq(model="llama-3.1-70b-versatile")
chat = ChatGroq(model="llama-3.1-8b-instant")
chain = prompt | chat


category = []
for transaction in list(df["Descrição"].values):
    category += [chain.invoke(transaction).content]

# base_url = ""    
# client = OpenAI(api_key="no-needed", base_url=base_url)
# model = client.models.list().data[0].id

# chat = ChatOpenAI(
#     temperature=0.0,
#     model=model,
#     base_url=base_url,
#     api_key="no-needed")

# chain = prompt | chat

# categorias = chain.batch(list(df["Descrição"].values))
df["Categorias"] = category
df.to_csv("finances.csv")