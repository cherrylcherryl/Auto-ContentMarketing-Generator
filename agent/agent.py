import os
from apikey import OPENAI_API_KEY, SERPER_API_KEY
from langchain.agents import tools, load_tools
from langchain.llms import OpenAI
from config.supported import AGENT_TOOLS
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

os.environ["SERPER_API_KEY"] = SERPER_API_KEY

from langchain.agents import initialize_agent, AgentType

class Agent:
    def __init__(self, llm : ChatOpenAI, tools : list[str]):
        self.llm = llm
        
        for tool in tools:
            assert tool in AGENT_TOOLS, "Unsupported tools!"
        
        self.tools = load_tools(tools)
        self.agent = initialize_agent(
            tools= self.tools,
            llm= self.llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
    
    def answer(self, prompt):
        answer = self.agent.run(prompt)
        return answer
        