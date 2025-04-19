from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from fastapi import UploadFile
import uuid
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_upload_file(upload_file: UploadFile) -> str:
    file_extension = upload_file.filename.split(".")[-1]
    file_name = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, file_name)
    
    with open(file_path, "wb") as buffer:
        content = await upload_file.read()
        buffer.write(content)
    
    return file_path

def generate_pdf(content: str, output_path: str):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # Simple text formatting
    textobject = c.beginText()
    textobject.setTextOrigin(50, height - 50)
    textobject.setFont("Helvetica", 12)
    
    # Split content into lines and add to PDF
    for line in content.split('\n'):
        textobject.textLine(line)
    
    c.drawText(textobject)
    c.save() 