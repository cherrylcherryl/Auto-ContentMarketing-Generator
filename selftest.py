from chat.dynamic_chat import LLMDynamicChat
from viewmodel.model import CompanyInfo

model = LLMDynamicChat()
company = CompanyInfo(
    name="FPT",
    domain="Retail",
    socialMedia="Facebook"
)
res = model.auto_analysis_company(company, False)
print(res)