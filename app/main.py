from fastapi import FastAPI
from app.api.routes_resume import router as resume_router
from app.api.routes_jd import router as jd_router

app = FastAPI()

app.include_router(resume_router, prefix="/resume")
app.include_router(jd_router, prefix="/jd")

@app.get("/")
def home():
    return {"message": "ATS Optimizer Running"}