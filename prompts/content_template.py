from langchain.prompts import PromptTemplate

class ContentGeneratorPrompt:
    def __init__(self):
        self.templates = [
            PromptTemplate(
                input_variables=[],
                template='''
                
                '''
            ),
        ]


        

    def get_content_generator_prompt(self, **kwargs) -> str:
        pass