from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from typing import Union
from langchain.memory import ConversationSummaryBufferMemory, ConversationBufferMemory


from apikey import load_env

OPENAI_API_KEY, SERPER_API_KEY = load_env()

class SearchAgent:
    def __init__(
        self,
        llm : Union[ChatOpenAI, OpenAI],
        temperature : float = 0.0,
        base_memory : Union[ConversationSummaryBufferMemory, ConversationBufferMemory] = None
    ):
        self.search = GoogleSerperAPIWrapper()
        if llm is None:
            llm = OpenAI(temperature=temperature)
        self.llm = llm

        tools = [
        Tool(
                name="Intermediate Answer",
                func=self.search.run,
                description="useful for when you need to ask with search"
            )
        ]
       
        if base_memory is None:
            self.memory = ConversationBufferMemory()
            self.agent = initialize_agent(
                tools=tools,
                llm = self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
                memory= self.memory
            )
        else:
            self.memory = base_memory
            self.agent = initialize_agent(
                tools=tools,
                llm = self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
                memory = self.memory
            )
    
    def answer(
            self,
            prompt : str,
            returning_memory = False
    ) -> str:
        answer = self.agent.run(prompt)
        if returning_memory:
            return answer, self.memory
        return answer
