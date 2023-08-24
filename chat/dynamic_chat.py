from langchain.chat_models import ChatOpenAI
from prompts.auto_generator import (
    AutoMarketAnalysisPromptGenerator, 
    AutoCompetitorAssessmentPromptGenerator,
    AutoDetectUniqueSellingPointPromptGenerator, 
    AutoContentCreationPromptGenerator
)
from agent.agent import Agent
from viewmodel.model import CompanyInfo
from typing import Union, Tuple, Any, List



class LLMDynamicChat:
    def __init__(
            self,
            llms : List[ChatOpenAI],
            agent: Agent | None = None,
    ):
        
        self.llms = llms
        
        market_analysis_prompt_generator = AutoMarketAnalysisPromptGenerator(llm=self.llms[0%len(self.llms)])
        competitor_analysis_prompt_generator = AutoCompetitorAssessmentPromptGenerator(llm=self.llms[1%len(self.llms)])
        selling_point_analysis_prompt_generator = AutoDetectUniqueSellingPointPromptGenerator(llm=self.llms[2%len(self.llms)])
        content_creation_prompt_generator = AutoContentCreationPromptGenerator(llm=self.llms[3%len(self.llms)])

        if agent is None:
            agent = Agent(
                llm = self.llms[0],
                tools=["google-serper"],
            )

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
        self.agent.switch_agent(self.llms[1%len(self.llms)])
        competitor_analysis = self.agent.answer(competitor_prompt)

        selling_point_prompt = self.selling_point_analysis_prompt_generator.generate_dynamic_prompt(domain=companyInfo.domain, competitor_analysis=competitor_analysis)
        self.agent.switch_agent(self.llms[2%len(self.llms)])
        selling_point_analysis, memory= self.agent.answer(selling_point_prompt, returning_memory=returning_memory)

        companyResearchInfo = {
            "market_analysis": market_analysis,
            "competitor": competitor_analysis,
            "key_selling_point": selling_point_analysis
        }

        return companyResearchInfo, memory
        
            