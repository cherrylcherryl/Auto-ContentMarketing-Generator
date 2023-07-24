
from langchain import PromptTemplate

MARKET_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["domain"],
    template='''
    My company is working on {domain}, in this market what is my chance and challenge
    Reply with a valid json format:
    {
        "chance": the chance of my company in this market, reply with list format as [chance_1, chance_2, ... , chance_n],
        "challenge": the challenge of my company, reply with list format as [challenge_1, challenge_2, ... , challenge_n]
    } 
    '''
)

COMPETITORS_PROMPT = PromptTemplate(
    input_variables=["company"],
    template='''My company is {company}, what are top 10 competiors of my companies
    Reply with a valid list of json format:
    [
        {
            "Name": the name of competitor_1,
            "Reason": the reason that you said it is my conpetitor_1
        },
        ...
        {
            "Name": the name of competitor_n,
            "Reason": the reason that you said it is my conpetitor_n 
        }
    ]
    '''
)

