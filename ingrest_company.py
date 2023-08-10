from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document

import json
import pandas as pd
import ast

from typing import List

from apikey import load_env

OPENAI_API_KEY, SERPER_API_KEY = load_env()

def load_data_company(
        data_path : str = "data/custom/company_reviews.csv"
) -> List[Document]:
    df = pd.read_csv(data_path, encoding='utf-8')
    df.fillna("", inplace=True)
    documents = []

    for (_, row) in df.iterrows():
        review = row["name"] + " is a company working on" + row["industry"] + ". " + row["description"]
        specs = dict()
        specs.update(ast.literal_eval(row["happiness"]))
        specs.update(ast.literal_eval(row["ratings"]))
        specs.update(ast.literal_eval(row["roles"]))
        specs["industry"] = row["industry"]
        specs["name"] = row["name"]
        document = Document(
            page_content=review,
            metadata=specs
        )
        documents.append(document)

    return documents
    
def ingrest_data(
        documents : List[Document],
        embeddings : OpenAIEmbeddings, 
        path : str = "data/integrated/company_reviews"
) -> None:
    instance = Chroma(embedding_function=embeddings, persist_directory=path)
    instance.add_documents(documents=documents)
    instance.persist()
        

if __name__ == '__main__':
    documents = load_data_company()
    embeddings = OpenAIEmbeddings(
        model="gpt-3.5-turbo",
        openai_api_key=OPENAI_API_KEY
    )
    ingrest_data(
        documents=documents,
        embeddings=embeddings
    )

    
    