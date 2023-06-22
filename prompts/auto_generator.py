from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


from apikey import OPENAI_API_KEY

class AutoMarketAnalysisPromptGenerator:
    def __init__(
            self, 
            llm : ChatOpenAI | None = None, 
            data_path : str = 'data/integrated/market_analysis'
    ):
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        chroma_instance = Chroma(persist_directory=data_path, embedding_function=embeddings)
        if llm is None:
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

    def generate_dynamic_prompt(
            self, 
            domain : str
    ) -> str:
        knowledge = "senior in {}".format(domain)
        prompt = self.qa_model.run(self.prompt_template.format(domain, knowledge))
        return prompt


class AutoCompetitorAssessmentPromptGenerator:
    def __init__(
            self, llm : ChatOpenAI | None = None, 
            data_path : str = 'data/integrated/competitor_assessments'
    ):
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        chroma_instance = Chroma(persist_directory=data_path, embedding_function=embeddings)
        if llm is None:
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
            I will provide you some information about the market analysis. You can use this information to construct the prompt.
            Here is the market analysis info: "{1}"
            The prompt must guide chatgpt to auto find some competitor. if chatgpt can not know many competitor, he must search on google. 
            The paragraph must contain "Suppose that you are a senior in data analysis".
        '''

    def generate_dynamic_prompt(
            self, 
            domain : str, 
            market_analysis_info : str
    ) -> str:
        prompt = self.qa_model.run(self.prompt_template.format(domain, market_analysis_info))
        return prompt
    
class AutoDetectUniqueSellingPointPromptGenerator:
    def __init__(
            self, llm : ChatOpenAI | None = None, 
            data_path : str = 'data/integrated/unique_selling_point'
    ):
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        chroma_instance = Chroma(persist_directory=data_path, embedding_function=embeddings)
        if llm is None:
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
            The role is detect unique selling point about {0}.
            Your goal is try to generate a good prompt that it can help chatgpt can analysis the unique selling point.
            I will provide you some information about the competitor assessment, you can use this information to generate prompt.
            Here is the competitor analysis "{1}"
            The paragraph must contain "I wolud like you to act as".
        '''

    def generate_dynamic_prompt(
            self, 
            domain : str, 
            competitor_analysis: str
    ) -> str:
        prompt = self.qa_model.run(self.prompt_template.format(domain, competitor_analysis))
        return prompt
    

class AutoContentCreationPromptGenerator:
    def __init__(
            self, 
            llm : ChatOpenAI | None = None, 
            data_path : str = 'data/integrated/content_creator'
    ):
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        chroma_instance = Chroma(persist_directory=data_path, embedding_function=embeddings)
        if llm is None:
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
            The role is craete a post in social media like {0}, the post must be most attracted to reader.
            Your goal is try to generate a good prompt that it can help chatgpt to creat a content marketing in social media.
            You must supply information about the "market analysis", "competitor assessment" and "unique selling point" in your prompt.
            Here is addition information, you can summarize this before craft prompt:
            Market Analysis: {1}.
            Competitor assesment: {2}.
            Unique selling point: {3}
            The paragraph must contain "I wolud like you to act as professional content create in {4}".
        '''

    def generate_dynamic_prompt(
            self, media : str, 
            market_analysis: str, 
            competitor_analysis : str, 
            selling_point : str
    ) -> str:
        prompt = self.qa_model.run(self.prompt_template.format(media, market_analysis, competitor_analysis, selling_point))
        return prompt
    