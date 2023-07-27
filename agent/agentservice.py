from config.config import BaseConfig
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from chat.dynamicchat import LLMDynamicChat
from chat.staticchat import LLMStaticChat
from chat.chatservice import ChatService
from typing import Union, Literal, Tuple, Any, Optional
from viewmodel.model import CompanyInfo, CompanyAnalysis
from apikey import OPENAI_API_KEY
class AgentService:
    def __init__(
            self,
            config : BaseConfig
    ):
        self.config = config

        if self.config.chat == False:
            self.llm = OpenAI(
                model=self.config.model,
                temperature=self.config.temperature,
                verbose=self.config.logging,
                openai_api_key=OPENAI_API_KEY
            )
        else:
            self.llm = ChatOpenAI(
                model=self.config.model,
                temperature=self.config.temperature,
                verbose=self.config.logging,
                openai_api_key=OPENAI_API_KEY
            )

        if self.config.dynamic == True:
            self.analizer = LLMDynamicChat(
                llm = self.llm,
                temperature=self.config.temperature
            )
        else:
            self.analizer = LLMStaticChat(
                llm = self.llm,
                temperature=self.config.temperature
            )

        self.creator = ChatService(
            llm=self.llm,
            temperature=self.config.temperature
        )

    def do_analysis(
            self,
            companyInfo : CompanyInfo
    ) -> Union[dict, Tuple[dict, Any]]:
        if self.config.dynamic:
            info, memory = self.analizer.auto_analysis_company(
                companyInfo=companyInfo,
                returning_memory=True
            )
            return info, memory
        else:
            info = self.analizer.company_analysis(
                company=companyInfo.name,
                domain=companyInfo.domain
            )
            return info

    def do_create_post(
            self,
            companyAnalysis : CompanyAnalysis,
            memory : Optional[Any]
    ) -> str:
        pass
