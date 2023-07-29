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

@app.post("/analysis/conpany-analysis")
async def company_analysis(companyInfo : CompanyInfo):
    config = BaseConfig()
    service = AgentService(config=config)
    info = service.do_analysis(companyInfo=companyInfo)
    return info

@app.post("/analysis/create-content")
async def create_marketing_content(companyAnalysis : CompanyAnalysis):
    pass

@app.post("/creator/create-content")
async def auto_create_content(companyInfo : CompanyInfo):
    pass

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)