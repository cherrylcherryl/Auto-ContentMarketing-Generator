
class BaseConfig:
    def __init__(
            self,
            name : str,
            model : str = 'gpt-3.5-turbo',
            temperature : float = 0.0,
            chat : bool = False,
            dynamic : bool = False,
            logging : bool = True
    ):
        self.name = name
        self.model = model
        self.temperature = temperature
        self.chat = chat
        self.dynamic = dynamic
        self.logging = logging