from pydantic import BaseModel
from typing import Optional, Literal

class ConpanyInfo(BaseModel):
    name : str
    domain : str
    website : Optional[str] = None
    tone : Literal["funny", "serious"] = "funny"
    socialMedia : Literal["Facebook", "Twitter", "Reddit"] = "Facebook"
    
