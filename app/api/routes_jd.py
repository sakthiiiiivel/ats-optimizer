from fastapi import APIRouter, Body
from app.services.jd_service import analyze_jd

router = APIRouter()

@router.post("/analyze")
async def analyze_job_description(payload: dict = Body(...)):
    jd_text = payload.get("jd_text", "")
    return analyze_jd(jd_text)