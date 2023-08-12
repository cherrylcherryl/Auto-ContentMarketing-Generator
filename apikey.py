import os
from typing import Tuple


def load_env() -> Tuple[str, str]:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY", "e7ce86460e7210bef65bf76c1b4432800c9152dc")

    #OPENAI_API_KEY = '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'
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    os.environ["SERPER_API_KEY"] = SERPER_API_KEY
    return OPENAI_API_KEY, SERPER_API_KEY