import os
from apikey import OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
from langchain.chat_models import ChatOpenAI
from prompts.auto_generator import (
    AutoMarketAnalysisPromptGenerator, 
    AutoCompetitorAssessmentPromptGenerator,
    AutoDetectUniqueSellingPointPromptGenerator, 
    AutoContentCreationPromptGenerator
)
from agent.agent import Agent
from langchain.schema import AIMessage, HumanMessage, SystemMessage

class LLMSequentialChatModel:
    def __init__(
            self,
            llm : ChatOpenAI | None = None,
            agent: Agent | None = None,
            market_analysis_prompt_generator : AutoMarketAnalysisPromptGenerator | None = None,
            competitor_analysis_prompt_generator : AutoCompetitorAssessmentPromptGenerator | None = None,
            selling_point_analysis_prompt_generator : AutoDetectUniqueSellingPointPromptGenerator | None = None,
            content_creation_prompt_generator : AutoContentCreationPromptGenerator | None = None,
            temperature : float = 0.0
    ):
        if llm is None:
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo", 
                temperature=temperature, 
                openai_api_key=OPENAI_API_KEY
            )
        if market_analysis_prompt_generator is None:
            market_analysis_prompt_generator = AutoMarketAnalysisPromptGenerator()
        if competitor_analysis_prompt_generator is None:
            competitor_analysis_prompt_generator = AutoCompetitorAssessmentPromptGenerator()
        if selling_point_analysis_prompt_generator is None:
            selling_point_analysis_prompt_generator = AutoDetectUniqueSellingPointPromptGenerator()
        if content_creation_prompt_generator is None:
            content_creation_prompt_generator = AutoContentCreationPromptGenerator()

        if agent is None:
            agent = Agent(
                llm = llm,
                tools=["google-serper"],
            )
        
        self.llm = llm
        self.market_analysis_prompt_generator = market_analysis_prompt_generator
        self.competitor_analysis_prompt_generator = competitor_analysis_prompt_generator
        self.selling_point_analysis_prompt_generator = selling_point_analysis_prompt_generator
        self.content_creation_prompt_generator = content_creation_prompt_generator
        self.agent = agent

    def auto_create_content(
            self,
            domain: str,
            social_media: str,
            **kwargs
    ) -> str: 
        
        market_analysis_prompt = self.market_analysis_prompt_generator.generate_dynamic_prompt(domain=domain)
        market_analysis = self.agent.answer(market_analysis_prompt)
        competitor_prompt = self.competitor_analysis_prompt_generator.generate_dynamic_prompt(domain=domain, market_analysis_info=market_analysis)
        competitor_analysis = self.agent.answer(competitor_prompt)
        selling_point_prompt = self.selling_point_analysis_prompt_generator.generate_dynamic_prompt(domain=domain, competitor_analysis=competitor_analysis)
        selling_point_analysis = self.agent.answer(selling_point_prompt)
        content_creator_prompt = self.content_creation_prompt_generator.generate_dynamic_prompt(social_media)
        # message = [
        #     SystemMessage(
        #     content='''
        #     Image that you are a professional content creator to creat a post in social media.
        #     Goal: create a post in social media with #hastag and many format that is commonly in this media. The format would be dynamic and based on your knowledge.
        #     Resource: you will be provide information about "market analysis", "competitor assessment" and "unique selling point".
        #     Constraints: ~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files.
        #     Output need only return the post content.
        #     '''
        #     ),
        #     SystemMessage(
        #     content=f'Market analysis: {market_analysis}'
        #     ),
        #     SystemMessage(
        #     content=f'Competitor assessment: {competitor_analysis}'
        #     ),
        #     SystemMessage(
        #     content=f'Unique selling point: {selling_point_analysis}'
        #     ),
        #     HumanMessage(
        #     content=content_creator_prompt
        #     )
        # ]

        content_created = self.agent.answer(content_creator_prompt)

        return content_created
        
            