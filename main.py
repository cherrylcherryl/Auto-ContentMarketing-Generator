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
    config = BaseConfig(language=CompanyAnalysis.language)
    service = AgentService(config=config)
    post = service.do_create_post(companyAnalysis=companyAnalysis)
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