
def add_language(
        language : str,
        base_prompt : str,
) -> str:
    lang_prompt = f"Reply with the following language. Language: {language}"
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
        Reply with a valid json format:
        {
            "chance": the chance of my company in this market, reply with a list format as ["chance_1", "chance_2", ... , "chance_n"], each element is a string format so put it on quotes \n
            "challenge": the challenge of my company, reply with a list format as ["challenge_1", "challenge_2", ... , "challenge_n"], each element is a string format so put it on quotes \n
        } 
        '''
    return base_prompt + constraint

def add_competitor_analysis_constraint(
        base_prompt : str
) -> str:
    constraint = '''\n
        Reply with a valid json format:
        {
                [
                        {
                                "number": 1,
                                "name": the name of competitor_1,
                                "reason": the reason that you said it is my conpetitor_1
                        },
                        ...
                        {
                                "number": n,
                                "name": the name of competitor_n,
                                "reason": the reason that you said it is my conpetitor_n 
                        }
                ]
        }
        '''
    return base_prompt + constraint

def add_key_selling_point_analysis_constraint(
        base_prompt : str
) -> str:
    constraint = '''\n
        Reply with a valid json format consit of a list of json object as:
        {
                [
                        {
                                "number": 1,
                                "name": key selling point name,
                                "reason": explain for what you said that is key selling point,
                        },
                        ...
                ]
        }
        '''
    return base_prompt + constraint