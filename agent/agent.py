import os
from apikey import OPENAI_API_KEY, SERPER_API_KEY
from langchain.agents import tools, load_tools
from langchain.llms import OpenAI
from config.supported import AGENT_TOOLS
from langchain.agents import initialize_agent, AgentType, AgentExecutor, ZeroShotAgent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory
from langchain import LLMChain

os.environ["SERPER_API_KEY"] = SERPER_API_KEY

from langchain.agents import initialize_agent, AgentType

class Agent:
    def __init__(self, llm : ChatOpenAI, tools : list[str]):
        self.llm = llm
        
        for tool in tools:
            assert tool in AGENT_TOOLS, "Unsupported tools!"

        self.tools = load_tools(tools)
        # self.prompt = ZeroShotAgent.create_prompt(self.tools)
        self.memory = ConversationSummaryBufferMemory(llm=self.llm, max_token_limit=10)
        
        # llm_chain = LLMChain(llm=self.llm, prompt=self.prompt)
        # agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
        # agent_chain = AgentExecutor.from_agent_and_tools(
        #     agent=agent, 
        #     tools=self.tools, 
        #     verbose=True, 
        #     memory=self.memory
        # )
        # self.agent = agent_chain
        
        self.agent = initialize_agent(
            tools= self.tools,
            llm= self.llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            memory= self.memory
        )
    
    def answer(self, prompt, returning_memory = False):
        answer = self.agent.run(prompt)
        if returning_memory:
            return answer, self.memory
        return answer
        