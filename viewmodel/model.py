from pydantic import BaseModel
from typing import Optional, Literal, Union, List

class CompanyInfo(BaseModel):
    name : str
    domain : str
    website : Optional[str] = None
    tone : Literal["funny", "serious"] = "funny"
    socialMedia : Literal["Facebook", "Twitter", "Reddit", "Tiktok", "Instagram"] = "Facebook"
    startup : bool = False
    language : Literal["English", "Vietnamese"]

class CompanyAnalysis(BaseModel):
    market_analysis: Union[str, dict, List[dict], list]
    competitor : Union[str, list, dict, List[dict]]
    key_selling_point : Union[str, list, dict, List[dict]]
    socialMedia : Literal["Facebook", "Twitter", "Reddit", "Tiktok", "Instagram"] = "Facebook"
    language : Literal["English", "Vietnamese"]
    tone : Literal["funny", "serious"] = "funny"
    website : Optional[str] = None