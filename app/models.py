from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    file_path = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 