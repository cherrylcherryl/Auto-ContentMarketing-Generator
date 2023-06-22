from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader


from apikey import OPENAI_API_KEY

class AutoMarketAnalysisPromptGenerator:
    def __init__(self, data_path : str = 'data/integrated/market_analysis'):
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        chroma_instance = Chroma(persist_directory=data_path, embedding_function=embeddings)
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

        self.qa_model = RetrievalQA.from_chain_type(
            llm = llm,
            chain_type="stuff",
            retriever=chroma_instance.as_retriever()
        )

        self.prompt_template = '''
            Craft a paragraph of how chatgpt (address as you) supposed to act based on the role stated. 
            Provide expectation of the required scope, skillset and knowledge. 
            If there is no specific role found, use relative reference if necessary. 
            The role is market analysis about "{0}".
            Your goal is try to generate a good prompt that it can help chatgpt can in-depth analysis into the market.
            The paragraph must contain "Imagine that you are a {1} and you want to in-depth analysis about this market" and end with "If you could not how to start or continue, you can find answer on google search."
        '''

    def generate_dynamic_prompt(self, domain : str) -> str:
        knowledge = "senior in {}".format(domain)
        prompt = self.qa_model.run(self.prompt_template.format(domain, knowledge))
        return prompt


class AutoCompetitorAssessmentPromptGenerator:
    def __init__(self, data_path : str = 'data/integrated/competitor_assessments'):
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        chroma_instance = Chroma(persist_directory=data_path, embedding_function=embeddings)
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

        self.qa_model = RetrievalQA.from_chain_type(
            llm = llm,
            chain_type="stuff",
            retriever=chroma_instance.as_retriever()
        )

        self.prompt_template = '''
            Craft a paragraph of how chatgpt (address as you) supposed to act based on the role stated. 
            Provide expectation of the required scope, skillset and knowledge. 
            If there is no specific role found, use relative reference if necessary. 
            The role is competitor assessmens in "{0}" domain.
            Your goal is try to generate a good prompt that it can help chatgpt can analysis the competitor assessment.
            The prompt must giuld chatgpt to auto find some competitor. if chatgpt can not know many competitor, he must search on google. 
            The paragraph must contain "Suppose that you are a senior in data analysis".
        '''

    def generate_dynamic_prompt(self, domain : str) -> str:
        prompt = self.qa_model.run(self.prompt_template.format(domain))
        return prompt