# Project Structure

```
resumegptbackend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and routes
│   ├── database.py          # SQLite configuration
│   ├── models.py            # Resume data model
│   └── pdf_handler.py       # PDF processing and generation
├── tests/
│   ├── __init__.py
│   └── test_main.py         # API endpoint tests
├── docs/
│   ├── implementation_plan.md
│   ├── project_structure.md
│   └── bug_tracking.md
├── .env                     # Local environment variables
├── .env.example            # Example environment variables
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment configuration
└── README.md              # Quick start guide
```

## Core Components

### app/
- `main.py`: FastAPI application with all routes and business logic
- `database.py`: SQLite connection and session management
- `models.py`: Single Resume model for SQLite storage
- `pdf_handler.py`: PDF processing and generation utilities

### Configuration
- `.env`: Local environment variables
- `requirements.txt`: Core dependencies:
  - fastapi
  - uvicorn
  - sqlalchemy
  - python-multipart
  - reportlab
  - python-dotenv

## Development Workflow
1. Set up environment
2. Implement core functionality
3. Test endpoints
4. Deploy to Render 