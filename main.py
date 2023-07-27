from fastapi import FastAPI, HTTPException
import uvicorn
from viewmodel.model import CompanyInfo, CompanyAnalysis
from chat.service import ChatService

app = FastAPI()



@app.get('/version')
async def get_version():
    return '1.0'

@app.post("/analysis/conpany-analysis")
async def company_analysis(conpanyInfo : CompanyInfo):
    pass

@app.post("/analysis/create-content")
async def create_marketing_content(companyAnalysis : CompanyAnalysis):
    pass

@app.post("/creator/create-content")
async def auto_create_content(companyInfo : CompanyInfo):
    pass

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)