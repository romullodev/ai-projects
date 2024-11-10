import ofxparse 
import pandas as pd
import os
import time

def deleteAllFilesFrom(folder):
  for root, dir, files in os.walk(folder):
    for file in files:
      os.remove(os.path.join(root, file))

def saveFile(uploaded_file):
    # Define o diretório de destino (ajuste para o seu caso)
    save_directory = "LangChain_Projects/LLM_FINANCE/extratos"

    # Cria o diretório se ele não existir
    os.makedirs(save_directory, exist_ok=True)

    # Gera um nome único para o arquivo (opcional)
    file_name = f"arquivo_{time.time()}.ofx"

    # Caminho completo do arquivo a ser salvo
    save_path = os.path.join(save_directory, file_name)

    # Salva o arquivo
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

def generateCsvFile(selcted_model: str):
    df = pd.DataFrame()

    for extrato in os.listdir("LangChain_Projects/LLM_FINANCE/extratos"): 
        with open(f'LangChain_Projects/LLM_FINANCE/extratos/{extrato}', encoding='ISO-8859-1') as ofx_file:
            ofx = ofxparse.OfxParser.parse(ofx_file)
        
        transaction_data = []
        for account in ofx.accounts: 
            for transaction in account.statement.transactions: 
                transaction_data.append({
                    "Data": transaction.date,
                    "Valor": transaction.amount,
                    "Descrição": transaction.memo,
                })

    df_temp = pd.DataFrame(transaction_data)
    df_temp["Valor"] = df_temp["Valor"].astype(float)
    df_temp["Data"] = df_temp["Data"].apply(lambda x: x.date())
    df = pd.concat([df, df_temp])

    # ========================================
    # LLM
    from langchain_groq import ChatGroq
    from langchain_core.prompts import PromptTemplate
    from dotenv import load_dotenv, find_dotenv

    _ = load_dotenv(find_dotenv())

    template = """
    Você é um analista de dados trabalhando em um projeto de limpeza de dados.
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

    Responda apenas com a categoria. Não esqueça disso.
    """

    prompt = PromptTemplate.from_template(template=template)
    chat = ChatGroq(model=selcted_model)
    chain = prompt | chat


    category = []
    for transaction in list(df["Descrição"].values):
        category += [chain.invoke(transaction).content]

    # run in parallel
    # categorias = chain.batch(list(df["Descrição"].values))
    df["Categorias"] = category
    print(df)
    df.to_csv("LangChain_Projects/LLM_FINANCE/finance.csv", index=False)