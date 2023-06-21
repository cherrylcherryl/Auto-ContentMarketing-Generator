from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import WebBaseLoader
from apikey import OPENAI_API_KEY
import os
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
import nest_asyncio
nest_asyncio.apply()
tgt_sites = [
    'https://github.com/f/awesome-chatgpt-prompts',
    'https://www.greataiprompts.com/prompts/best-system-prompts-for-chatgpt/',
    'https://stackdiary.com/chatgpt/role-based-prompts/',
    'https://clickup.com/templates/ai-prompts/market-research-and-analysis',
    'https://snackprompt.com/topic/marketing/',
    'https://snackprompt.com/prompt/in-depth-market-research-data-analysis',
    'https://snackprompt.com/prompt/market-research',
    'https://snackprompt.com/prompt/in-depth-market-research-insights'
]


def add_documents(loader, instance):
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators= ["\n\n", "\n", ".", ";", ",", " ", ""])
    texts = text_splitter.split_documents(documents)
    instance.add_documents(texts)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
instance = Chroma(embedding_function=embeddings, persist_directory='data')

loader = WebBaseLoader(tgt_sites)
if loader:
    add_documents(loader, instance)

instance.persist()