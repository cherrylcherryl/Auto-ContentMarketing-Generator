from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import initialize_agent, AgentType, load_tools, Tool
from prompts.analysis_template import StaticPromptTemplate
from typing import Callable, Union, Any, Tuple, List
from agent.agent import Agent
from agent.agent_search import SearchAgent
from langchain.memory import ConversationSummaryBufferMemory, ConversationBufferMemory


class LLMStaticChat:
    def __init__(
            self,
            llms : List[ChatOpenAI],
    ):

        self.llms = llms
        
        self.agent = Agent(
                llm = self.llms[0],
                tools=["google-serper"],
            )

    
    def company_analysis(
            self,
            company : str,
            domain: str,
    ) -> dict: 
        prompt_template = StaticPromptTemplate()
        company_analysis = dict()
        company_analysis["market_analysis"] = self.run_agent(
            prompt=prompt_template.get_market_analysis_prompt(company, domain)
        )
        self.agent.switch_agent(self.llms[1%len(self.llms)])
        company_analysis["competitor"] = self.run_agent(
            prompt=prompt_template.get_competitor_prompt(company)
        )
        self.agent.switch_agent(self.llms[2%len(self.llms)])
        company_analysis["key_selling_point"], memory = self.run_agent(
           prompt=prompt_template.get_key_selling_point(company),
           returning_memory=True
        )

        return company_analysis, memory

    def run_agent(
            self,
            prompt : str,
            returning_memory : bool = False
    ) -> Tuple[str,Union[ConversationSummaryBufferMemory, ConversationBufferMemory]] :
        if returning_memory:
            response, memory = self.agent.answer(prompt, returning_memory=returning_memory)
            return response, memory
        else:
            response = self.agent.answer(prompt, returning_memory=returning_memory)
            return response
