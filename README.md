# ResumeGPT Backend

A FastAPI backend service for handling resume PDFs.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /resume/upload`: Upload a PDF resume
- `GET /resume/{id}`: Get resume metadata
- `GET /resume/{id}/pdf`: Download the resume PDF

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 