from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from typing import Union, List
from apikey import load_env
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory, ConversationBufferMemory


OPENAI_API_KEY, SERPER_API_KEY = load_env()

class ChatService:
    def __init__(
            self,
            llm : Union[ChatOpenAI, OpenAI],
            memory : Union[ConversationSummaryBufferMemory, ConversationBufferMemory]
    ):
        self.conversation = ConversationChain(
            llm=llm, 
            verbose=True, 
            memory=memory
        )

    def chat(
            self,
            prompt,
    ) -> str:
        #response = self.llm(messages=prompt)
        response = self.conversation.predict(input=prompt)
        return response
