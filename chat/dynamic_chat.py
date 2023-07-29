import os
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from prompts.auto_generator import (
    AutoMarketAnalysisPromptGenerator, 
    AutoCompetitorAssessmentPromptGenerator,
    AutoDetectUniqueSellingPointPromptGenerator, 
    AutoContentCreationPromptGenerator
)
from agent.agent import Agent
from viewmodel.model import CompanyInfo
from typing import Union, Tuple, Any

from apikey import load_env
OPENAI_API_KEY, SERPER_API_KEY = load_env()
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

class LLMDynamicChat:
    def __init__(
            self,
            llm : OpenAI | ChatOpenAI | None = None,
            agent: Agent | None = None,
            market_analysis_prompt_generator : AutoMarketAnalysisPromptGenerator | None = None,
            competitor_analysis_prompt_generator : AutoCompetitorAssessmentPromptGenerator | None = None,
            selling_point_analysis_prompt_generator : AutoDetectUniqueSellingPointPromptGenerator | None = None,
            content_creation_prompt_generator : AutoContentCreationPromptGenerator | None = None,
            temperature : float = 0.0
    ):
        if llm is None:
            llm = OpenAI(
                model_name="gpt-3.5-turbo", 
                temperature=temperature, 
                openai_api_key=OPENAI_API_KEY
            )
        self.llm = llm
        if market_analysis_prompt_generator is None:
            market_analysis_prompt_generator = AutoMarketAnalysisPromptGenerator(llm=self.llm)
        if competitor_analysis_prompt_generator is None:
            competitor_analysis_prompt_generator = AutoCompetitorAssessmentPromptGenerator(llm=self.llm)
        if selling_point_analysis_prompt_generator is None:
            selling_point_analysis_prompt_generator = AutoDetectUniqueSellingPointPromptGenerator(llm=self.llm)
        if content_creation_prompt_generator is None:
            content_creation_prompt_generator = AutoContentCreationPromptGenerator(llm=self.llm)

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

    def auto_analysis_company(
            self,
            companyInfo : CompanyInfo,
            returning_memory : bool = True
    ) -> Union[dict, Tuple[dict, Any]]: 
        
        market_analysis_prompt = self.market_analysis_prompt_generator.generate_dynamic_prompt(domain=companyInfo.domain)
        market_analysis = self.agent.answer(market_analysis_prompt)
        
        competitor_prompt = self.competitor_analysis_prompt_generator.generate_dynamic_prompt(domain=companyInfo.domain)
        competitor_analysis = self.agent.answer(competitor_prompt)

        # competitor_analysis = '''
        # 1. Competitors:
        # - Printful: Printful is one of the most popular print-on-demand companies. They offer over 220 different products and provide a wide range of services.
        # - Printify: Printify is a major competitor to Printful. They offer a similar range of products and services for print on demand.

        # 2. Strategies:
        # - Printful: Printful focuses on providing a wide variety of products and services to their customers. They have a user-friendly interface and offer integrations with popular e-commerce platforms.
        # - Printify: Printify also offers a wide range of products and services. They differentiate themselves by providing 
        # a large network of printing partners, allowing customers to choose the best option for their needs.

        # 3. Ads Strategies:
        # - Unfortunately, I couldn't find specific information about the advertising strategies of these competitors. However, it is common for print on demand companies to use online advertising platforms like Google Ads and social media ads to reach their target audience.

        # 4. Differentiators and Customer Experience:
        # - Printful: Printful differentiates itself by offering a wide range of products and services, as well as integrations with popular e-commerce platforms. They also provide excellent customer support and have a user-friendly interface.   - Printify: Printify differentiates itself by providing a large network of printing partners, giving customers more options and flexibility. They also offer competitive pricing and a user-friendly platform.

        # Overall, both Printful and Printify are popular print on demand competitors that offer a wide range of products and services. They differentiate themselves through their unique features and customer experiences. While I couldn't find specific information about their advertising strategies, it is common for print on demand companies to use online advertising platforms to reach their target audience.

        # '''

        selling_point_prompt = self.selling_point_analysis_prompt_generator.generate_dynamic_prompt(domain=companyInfo.domain, competitor_analysis=competitor_analysis)
        selling_point_analysis, memory= self.agent.answer(selling_point_prompt, returning_memory=returning_memory)
        #content_creator_prompt = self.content_creation_prompt_generator.generate_dynamic_prompt(social_media)
        
        
        
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

        companyResearchInfo = {
            "market_analysis": market_analysis,
            "competitor": competitor_analysis,
            "key_selling_point": selling_point_analysis
        }

        return companyResearchInfo, memory
        
            