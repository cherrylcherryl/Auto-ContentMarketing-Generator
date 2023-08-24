import os
from typing import Tuple, Union, List


def load_env(
        preservation_key : bool = False
) -> Union[Tuple[str, str], Tuple[str, str, List[str]]]:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY", "e7ce86460e7210bef65bf76c1b4432800c9152dc")
    OPENAI_API_KEYS = []

    if preservation_key:
        api_keys = os.getenv("OPENAI_API_KEYS", None)
        if api_keys is not None:
            api_keys = api_keys.split(";")
            if isinstance(api_keys, list):
                OPENAI_API_KEYS = api_keys
            
            
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    os.environ["SERPER_API_KEY"] = SERPER_API_KEY
    if preservation_key:
        return OPENAI_API_KEY, SERPER_API_KEY, OPENAI_API_KEYS
    return OPENAI_API_KEY, SERPER_API_KEY