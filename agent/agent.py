import os
from apikey import load_env
from langchain.agents import tools, load_tools
from langchain.llms import OpenAI
from config.supported import AGENT_TOOLS
from langchain.agents import initialize_agent, AgentType, AgentExecutor, ZeroShotAgent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory
from langchain import LLMChain
from agent.tools import search_company_db

OPENAI_API_KEY, SERPER_API_KEY = load_env()

from langchain.agents import initialize_agent, AgentType

class Agent:
    def __init__(
            self, llm : ChatOpenAI, 
            tools : list[str],
            use_memory : bool = False
        ):
        self.llm = llm
        
        for tool in tools:
            assert tool in AGENT_TOOLS, "Unsupported tools!"

        self.tools = load_tools(tools)
        tools.append(search_company_db)
        # self.prompt = ZeroShotAgent.create_prompt(self.tools)
        self.use_memory = use_memory
        if use_memory:
            self.memory = ConversationSummaryBufferMemory(llm=self.llm, max_token_limit=10)
            self.agent = initialize_agent(
                tools= self.tools,
                llm= self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
                memory= self.memory
            )
        else:
            self.agent = initialize_agent(
                tools= self.tools,
                llm= self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
            )
        
        
    
    def answer(self, prompt, returning_memory = False):
        answer = self.agent.run(prompt)
        if returning_memory and self.use_memory:
            return answer, self.memory
        return answer
        