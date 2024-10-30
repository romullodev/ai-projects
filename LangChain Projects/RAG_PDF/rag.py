from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from generate_db import get_db_retriever
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

prompt = ChatPromptTemplate.from_template("""Responda a pergunta com base apenas no contexto:
{context}
Pergunta: {input}
""")
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0)
document_chain = create_stuff_documents_chain(llm, prompt)
retriever_chain = create_retrieval_chain(get_db_retriever(), document_chain)
question = "qual o número máximo de convidados eu posso levar para uma reserva na churrasqueira?"
response = retriever_chain.invoke({"input": f"{question}"})
response_details = response['answer']

print(
    f"""
    Pergunta: {question}
    Responsa: {response_details}
""")