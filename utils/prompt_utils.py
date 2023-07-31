
def add_language(
        language : str,
        base_prompt : str,
) -> str:
    lang_prompt = f"Only reply with the valid language, the valid language is: {language}. If the answer not avaliable in {language}, you must translate it."
    lang_prompt = f'{base_prompt}\n{lang_prompt}'
    return lang_prompt

def add_website(
        website: str,
        base_prompt : str
) -> str:
    site_prompt = f'''
        You can look for your information about this company in website: {website}\n
    '''
    site_prompt = f'{base_prompt}\n{site_prompt}'
    return site_prompt

def add_market_analysis_constraint(
        base_prompt : str
) -> str:
    constraint = '''\n
        Reply with a format:
        "chance": the chance of my company in this market, reply with a format as 
        1. chance 1
        2. chance 2
        ...
        n. chance n
        "challenge": the challenge of my company, reply with a list format as 
        1. challenge 1
        2. challenge 2
        ...
        n. challenge n  
        '''
    return base_prompt + constraint

def add_competitor_analysis_constraint(
        base_prompt : str
) -> str:
    constraint = '''\n
        Give me a list of competitor base on the following format:
        1. Competitor 1: the reason you said that is my competitor
        2. Competitor 2: the reason you said that is my competitor
        ...
        n. Competitor n: the reason you said that is my competitor
        '''
    return base_prompt + constraint

def add_key_selling_point_analysis_constraint(
        base_prompt : str
) -> str:
    constraint = '''\n
        Give me a list of key selling point base on the following format:
        1. Key selling point 1: the reason you said that is my Key selling point
        2. Key selling point 2: the reason you said that is my Key selling point
        ...
        n. Key selling point n: the reason you said that is my Key selling point
        '''
    return base_prompt + constraint

def add_analysis_info(
        market_analysis : str,
        competitor : str,
        key_selling_point : str,
        base_prompt : str
) -> str :
    constraint = f'''
        You can use this additional information for create bester post.
        Market analysis : {market_analysis}\n
        Competitor: {competitor} \n
        Key selling point: {key_selling_point}\n
        '''
    return base_prompt + constraint