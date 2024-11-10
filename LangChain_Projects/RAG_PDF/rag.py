from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

def search(question, model_selected, db_retriever):
    prompt = ChatPromptTemplate.from_template("""Responda a pergunta com base apenas no contexto:
    {context}
    Pergunta: {input}
    """)
    llm = ChatGroq(model=model_selected, temperature=0.0)
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever_chain = create_retrieval_chain(db_retriever, document_chain)
    response = retriever_chain.invoke({"input": f"{question}"})
    response_details = response['answer']
    return response_details

# print(
#     f"""
#     Pergunta: {question}
#     Responsa: {response_details}
# """)