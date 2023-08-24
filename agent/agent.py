from langchain.agents import tools, load_tools
from config.supported import AGENT_TOOLS
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory, ConversationBufferMemory
from agent.tools import search_company_db
from typing import List, Union

from langchain.agents import initialize_agent, AgentType

class Agent:
    def __init__(
            self, 
            llm : ChatOpenAI, 
            tools : List[str],
            base_memory : Union[ConversationSummaryBufferMemory, ConversationBufferMemory] = None
    ):
        self.llm = llm
        
        for tool in tools:
            assert tool in AGENT_TOOLS, "Unsupported tools!"

        self.tools = load_tools(tools)
        tools.append(search_company_db)
        
        if base_memory is not None:
            self.memory = base_memory
            self.agent = initialize_agent(
                tools= self.tools,
                llm= self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
                memory= self.memory
            )
        else:
            self.memory = ConversationBufferMemory()
            self.agent = initialize_agent(
                tools= self.tools,
                llm= self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
                memory=self.memory
            )

    def switch_agent(
          self,
          llm : ChatOpenAI  
    ) -> None:
        self.agent = initialize_agent(
                tools= self.tools,
                llm= llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
                memory=self.memory
            )   
        
    def answer(self, prompt, returning_memory = False):
        answer = self.agent.run(prompt)
        if returning_memory:
            return answer, self.memory
        return answer
        