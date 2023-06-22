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
            **kwargs
    ) -> str: 
        
        prompt = self.market_analysis_prompt_generator.generate_dynamic_prompt(domain=domain)
        res = self.agent.answer(prompt)
        return res
        
            