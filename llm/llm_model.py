import os
from apikey import OPENAI_API_KEY
from langchain.llms import OpenAI
from config.supported import CHAT_MODELS

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

class LLM:
    def __init__(self, llm_name: str, temperature : float):
        self.name = llm_name
        self.temperature = temperature

        self.llm = self.load_llm_model()
    def load_llm_model(self) -> OpenAI: 
        assert self.name in CHAT_MODELS, "Unsupported LLM chat models!"
        llm = OpenAI(model=self.name, temperature=self.temperature)
        return llm
