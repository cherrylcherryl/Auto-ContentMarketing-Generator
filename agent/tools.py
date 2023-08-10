from langchain.agents import tool
from langchain.embeddings import OpenAIEmbeddings
from apikey import load_env
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

OPENAI_API_KEY, SERPER_API_KEY = load_env()

@tool("search_company_db", return_direct=False)
def search_company_db(
    query : str 
) -> str:
    '''
    You call this function at the first time when analysis the unique selling of the company.
    Note that the company maybe not in the database so this function will have a score to verify that the trustworthy of anwser.
    '''
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    chroma_instance = Chroma(persist_directory="data/integrated/company_reviews", embedding_function=embeddings)
    
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

    qa_model = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type="stuff",
        retriever=chroma_instance.as_retriever()
    )

    answer = qa_model.run(query)
    return answer
