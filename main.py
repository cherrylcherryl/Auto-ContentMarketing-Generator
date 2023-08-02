from fastapi import FastAPI, HTTPException
import uvicorn
from viewmodel.model import CompanyInfo, CompanyAnalysis
from chat.chat_service import ChatService
from agent.agent_service import AgentService
from config.config import BaseConfig
app = FastAPI()



@app.get('/version')
async def get_version():
    return '1.0'

@app.post("/analysis/company-analysis")
async def company_analysis(companyInfo : CompanyInfo):
    config = BaseConfig(language=companyInfo.language, dynamic=companyInfo.startup)
    service = AgentService(config=config)
    info, mem = service.do_analysis(companyInfo=companyInfo)
    return info

@app.post("/analysis/create-content")
async def create_marketing_content(companyAnalysis : CompanyAnalysis):
    config = BaseConfig(language=companyAnalysis.language)
    service = AgentService(config=config)

#     #Test data
#     companyAnalysis.market_analysis = '''
# "chance":
# 1. Market growth

# "challenge":
# 1. Setting and keeping up with deadlines
# 2. Client retention/reducing churn
# 3. Retaining quality talent
# 4. Standing out from the crowd
# 5. Finding and retaining the right people
# 6. Getting more customers
# 7. Providing proof of service before purchase
# 8. Poor planning and lack of staff training
# 9. Unrealistic expectations
# 10. Lean budgets
# 11. Pricing pressures
# 12. Measurement of PR
# 13. AI-generated content
# 14. Client-facing data quality

# '''
#     companyAnalysis.competitor = '''
# 1. Flibbr Consulting: They offer similar services and have a strong presence in the market.
# 2. Syncom Media: They have a similar target audience and offer competitive pricing.
# 3. Asymmetrique: They have a strong reputation in the industry and offer innovative solutions.

# '''
#     companyAnalysis.key_selling_point='''
# The key selling points of PMax's products are maximizing reach, utilizing machine learning for optimal performance, offering features for issue diagnosis and improvement, and providing goal-based automation.
# '''
    post = service.do_create_post(companyAnalysis=companyAnalysis)
    print(post)
    return post

@app.post("/creator/create-content")
async def auto_create_content(companyInfo : CompanyInfo):
    config = BaseConfig(language=companyInfo.language, dynamic=companyInfo.startup)
    service = AgentService(config=config)
    info, mem = service.do_analysis(companyInfo=companyInfo)

    companyAnalysis = CompanyAnalysis(
        name=companyInfo.name,
        market_analysis=info["market_analysis"],
        competitor=info["competitor"],
        key_selling_point=info["key_selling_point"],
        social_media=companyInfo.social_media,
        language=companyInfo.language,
        tone=companyInfo.tone,
        website=companyInfo.website
    )
    post = service.do_create_post(companyAnalysis)
    return post

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5001)