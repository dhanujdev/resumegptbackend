from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
from . import models, pdf_handler
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ResumeGPT Backend")

@app.post("/resume/upload")
async def upload_resume(
    file: UploadFile = File(...),
    title: str = "Untitled Resume",
    db: Session = Depends(get_db)
):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    file_path = await pdf_handler.save_upload_file(file)
    
    # Create resume record in database
    db_resume = models.Resume(
        title=title,
        content="",  # We'll extract content later if needed
        file_path=file_path
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    
    return {"id": db_resume.id, "message": "Resume uploaded successfully"}

@app.get("/resume/{resume_id}")
async def get_resume(resume_id: int, db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    return {
        "id": resume.id,
        "title": resume.title,
        "created_at": resume.created_at
    }

@app.get("/resume/{resume_id}/pdf")
async def get_resume_pdf(resume_id: int, db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    if not os.path.exists(resume.file_path):
        raise HTTPException(status_code=404, detail="PDF file not found")
    
    return FileResponse(
        resume.file_path,
        media_type="application/pdf",
        filename=f"resume_{resume_id}.pdf"
    ) 