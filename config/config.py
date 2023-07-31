
class BaseConfig:
    def __init__(
            self,
            name : str = 'AI',
            model : str = 'gpt-3.5-turbo',
            temperature : float = 0.0,
            dynamic : bool = False,
            logging : bool = True,
            language : str = "English",
            tone: str = "Funny",
            chat : bool = True
    ):
        self.name = name
        self.model = model
        self.temperature = temperature
        self.dynamic = dynamic
        self.logging = logging
        self.language = language
        self.tone = tone
        self.chat = chat