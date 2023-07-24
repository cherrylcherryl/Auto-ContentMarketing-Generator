import os
from apikey import OPENAI_API_KEY, SERPER_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY

from langchain.llms import OpenAI
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import initialize_agent, AgentType, load_tools, Tool

class LLMStaticChat:
    def __init__(
            self,
            llm : OpenAI | None = None,
            temperature : int = 0
    ):
        self.temperature = temperature
        if llm is None:
            llm = OpenAI(temperature=self.temperature, openai_api_key=OPENAI_API_KEY)
        self.llm = llm
        search = GoogleSerperAPIWrapper()
        tools = [
            Tool(
                name="Intermediate Answer",
                func=search.run,
                description="useful for when you need to ask with search"
            )
        ]

        self.agent = initialize_agent(
            tools = tools,
            llm = self.llm,
            agent = AgentType.SELF_ASK_WITH_SEARCH,
            verbose = True
        )
    
    def company_analysis(
            self,
            query : str
    ) -> dict: 
        pass
