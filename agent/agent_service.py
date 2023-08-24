from config.config import BaseConfig
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from chat.dynamic_chat import LLMDynamicChat
from chat.static_chat import LLMStaticChat
from chat.chat_service import ChatService
from typing import Union, Literal, Tuple, Any, Optional
from viewmodel.model import CompanyInfo, CompanyAnalysis
from prompts.content_template import ContentGeneratorPrompt
from apikey import load_env

OPENAI_API_KEY, SERPER_API_KEY, OPENAI_API_KEYS = load_env(preservation_key=True)


class AgentService:
    def __init__(
            self,
            config : BaseConfig
    ):
        self.config = config

        self.llms = []
        
        openai_llm_chat = ChatOpenAI(
            model=self.config.model,
            temperature=self.config.temperature,
            verbose=self.config.logging,
            openai_api_key=OPENAI_API_KEY
        )

        self.llms.append(openai_llm_chat)
        if len(OPENAI_API_KEYS) > 0:
            for API_KEY in OPENAI_API_KEYS:
                openai_llm_chat = ChatOpenAI(
                    model=self.config.model,
                    temperature=self.config.temperature,
                    verbose=self.config.logging,
                    openai_api_key=API_KEY
                )
                self.llms.append(openai_llm_chat)
    

        if self.config.dynamic == True:
            self.analizer = LLMDynamicChat(
                llms = self.llms,
            )
        else:
            self.analizer = LLMStaticChat(
                llms = self.llms,
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
            info, memory = self.analizer.company_analysis(
                company=companyInfo.name,
                domain=companyInfo.domain
            )
            return info, memory

    def do_create_post(
            self,
            companyAnalysis : CompanyAnalysis,
            memory : Optional[Any] = None
    ) -> str:
        creator = ChatService(
            llm=self.llms[1%len(self.llms)],
            memory=memory
        )
        template = ContentGeneratorPrompt()
        prompt = template.get_content_generator_prompt(companyAnalysis=companyAnalysis)
        post = creator.chat(prompt)
        print(post)
        return post
