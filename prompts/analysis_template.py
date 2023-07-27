
from langchain import PromptTemplate

class StaticPromptTemplate:
    def __init__(self):
        self.MARKET_ANALYSIS_PROMPT = PromptTemplate(
            input_variables=["domain"],
            template='''
            My company is working on {domain}, in this market what is my chance and challenge
            Reply with a valid json format:
            {
                "chance": the chance of my company in this market, reply with a list format as ["chance_1", "chance_2", ... , "chance_n"], each element is a string format so put it on quotes \n
                "challenge": the challenge of my company, reply with a list format as ["challenge_1", "challenge_2", ... , "challenge_n"], each element is a string format so put it on quotes \n
            } 
            '''
        )

        self.COMPETITORS_PROMPT = PromptTemplate(
            input_variables=["company"],
            template='''My company is {company}, what are top 10 competiors of my companies
            Reply with a valid list of json format:
            [
                {
                    "name": the name of competitor_1,
                    "reason": the reason that you said it is my conpetitor_1
                },
                ...
                {
                    "name": the name of competitor_n,
                    "reason": the reason that you said it is my conpetitor_n 
                }
            ]
            '''
        )

        self.KEY_SELLING_POINT = PromptTemplate(
            input_variables=["company"],
            template='''
            Act as a senior, you must be thinking carefully to answer this question.
            Your resource is not limited such as internet and google search.
            The question is: "What are the key selling points of {company}'s products? Try to generalize and not base it off one product."
            Reply with a valid json format consit of a list of json object as:
            [
                {
                    "name": key selling point name,
                    "reason": explain for what you said that is key selling point,
                },...
            ]
            '''
        )
    
    def get_market_analysis_prompt(
            self,
            domain : str
        ) -> str:
        prompt = self.MARKET_ANALYSIS_PROMPT.format(domain=domain)
        return prompt
    
    def get_competitor_prompt(
            self, 
            company : str
        ) -> str:
        prompt = self.COMPETITORS_PROMPT.format(company=company)
        return prompt
    
    def get_key_selling_point(
            self, 
            company : str
        ) -> str:
        prompt = self.KEY_SELLING_POINT.format(company=company)
        return prompt

