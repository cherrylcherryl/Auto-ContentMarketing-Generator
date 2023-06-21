import os
from apikey import OPENAI_API_KEY, SERPER_API_KEY
from langchain.agents import tools, load_tools
from langchain.llms import OpenAI
from llm.llm_model import LLM
from config.supported import AGENT_TOOLS
from langchain.agents import initialize_agent, AgentType

os.environ["SERPER_API_KEY"] = SERPER_API_KEY

from langchain.agents import initialize_agent, AgentType

class Agent:
    def __init__(self, llm : LLM, tools : list[str], search : bool = True):
        self.llm = llm
        
        for tool in tools:
            assert tool in AGENT_TOOLS, "Unsupported tools!"
        
        self.tools = load_tools(tools)
        self.agent_type = AgentType.SELF_ASK_WITH_SEARCH if search else AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
        self.agent = initialize_agent(
            tools= self.tools,
            llm= self.llm,
            agent=self.agent_type,
            verbose=True
        )
    
    def answer(self, prompt):
        answer = self.agent.run()
        