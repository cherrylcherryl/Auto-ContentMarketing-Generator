from langchain.chat_models import ChatOpenAI
from apikey import load_env
from langchain.schema import AIMessage, HumanMessage, SystemMessage

OPENAI_API_KEY, _ = load_env()

class EvaluationModel:
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            model='gpt-3.5-turbo',
            temperature=0.0,
            openai_api_key=OPENAI_API_KEY
        )
    def eval(
            self,
            company : str,
            field : str,
            content : str,
            info : dict
    ) -> str:
        message = []
        message.append(
            SystemMessage(
                content='Act as a professional content marketing creator.'
            )
        )
        message.append(
            AIMessage(
                content='Sure! I can analysis any thing with preference metrics.'
            )
        )
        message.append(
            SystemMessage(
                content='''
                Evaluate with these metric:
                - Content: the post must include information about company, field, chance and challenge in this market
                - Unique selling point: the post must include the unique selling point. 
                - CTA: included CTA
                '''
            )
        )

        message.append(
            HumanMessage(
                content=f'''
                I have create a post to promote my {company} company in {field} field.
                Here is my content created : {content}
                This content was make from some information:
                - Market analysis: {info['market_analysis']}
                - Competitor: {info['competitor']}
                - Key selling point: {info['key_selling_point']}
                '''
            )
        )