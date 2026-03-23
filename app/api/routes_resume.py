import os
import shutil
from uuid import uuid4
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.parser_service import extract_resume_text

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in [".pdf", ".docx"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX allowed")

    file_path = os.path.join(UPLOAD_DIR, f"{uuid4()}{ext}")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_resume_text(file_path)

    return {
        "filename": file.filename,
        "text_length": len(text),
        "preview": text[:500]
    }