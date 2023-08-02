from pydantic import BaseModel
from typing import Optional, Literal, Union, List

class CompanyInfo(BaseModel):
    name : str
    domain : str
    website : Optional[str] = None
    tone : str = "funny"
    social_media : str = "Facebook"
    startup : bool = False
    language : str = "english"

class CompanyAnalysis(BaseModel):
    name : str
    market_analysis: Union[str, dict, List[dict], list]
    competitor : Union[str, list, dict, List[dict]]
    key_selling_point : Union[str, list, dict, List[dict]]
    social_media : str = "Facebook"
    language : str = "english"
    tone : str = "funny"
    website : Optional[str] = None