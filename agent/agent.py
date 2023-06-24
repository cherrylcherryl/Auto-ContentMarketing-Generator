import os
from apikey import OPENAI_API_KEY, SERPER_API_KEY
from langchain.agents import tools, load_tools
from langchain.llms import OpenAI
from config.supported import AGENT_TOOLS
from langchain.agents import initialize_agent, AgentType, AgentExecutor, ZeroShotAgent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain import LLMChain

os.environ["SERPER_API_KEY"] = SERPER_API_KEY

from langchain.agents import initialize_agent, AgentType

class Agent:
    def __init__(self, llm : ChatOpenAI, tools : list[str]):
        self.llm = llm
        
        for tool in tools:
            assert tool in AGENT_TOOLS, "Unsupported tools!"

        self.tools = load_tools(tools)
        self.prompt = ZeroShotAgent.create_prompt(self.tools)
        self.memory = ConversationBufferMemory()
        
        llm_chain = LLMChain(llm=self.llm, prompt=self.prompt)
        agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
        agent_chain = AgentExecutor.from_agent_and_tools(
            agent=agent, 
            tools=self.tools, 
            verbose=True, 
            memory=self.memory
        )
        self.agent = agent_chain
        # self.agent = AgentExecutor.from_agent_and_tools(
        #     tools= self.tools,
        #     llm= self.llm,
        #     agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        #     memory=self.memory
        #     verbose=True
        # )
    
    def answer(self, prompt):
        answer = self.agent.run(prompt)
        return answer
        