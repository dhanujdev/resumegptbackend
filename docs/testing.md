# Testing Documentation

## Local Development Setup Tests

### Environment Setup
- [x] Virtual environment creation
- [x] Dependencies installation
- [x] Database initialization
- [x] Environment variables configuration

### API Endpoint Tests

#### 1. Resume Upload (POST /resume/upload)
```bash
curl -X POST "http://localhost:8000/resume/upload" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/Users/dhanujgumpella/Documents/projects/resumegptbackend/Gumpella_Dhanuj_Resume.pdf" \
     -F "title=Gumpella_Dhanuj_Resume"
```
**Result**: Success
- Status Code: 200
- Response: `{"id":1,"message":"Resume uploaded successfully"}`

#### 2. Get Resume Metadata (GET /resume/{id})
```bash
curl -X GET "http://localhost:8000/resume/1" -H "accept: application/json"
```
**Result**: Success
- Status Code: 200
- Response: `{"id":1,"title":"Untitled Resume","created_at":"2025-04-19T16:10:24"}`

#### 3. Download Resume PDF (GET /resume/{id}/pdf)
```bash
curl -X GET "http://localhost:8000/resume/1/pdf" \
     -H "accept: application/pdf" \
     --output downloaded_resume.pdf
```
**Result**: Success
- Status Code: 200
- File downloaded successfully

## Error Handling Tests

### 1. Invalid File Type
- Test: Upload non-PDF file
- Expected: 400 Bad Request
- Result: ✅ Passed

### 2. Non-existent Resume
- Test: Request non-existent resume ID
- Expected: 404 Not Found
- Result: ✅ Passed

## Deployment Configuration Tests

### Render Configuration
- [x] `render.yaml` created with correct settings
- [x] Environment variables configured
- [x] Disk storage configured for uploads
- [x] Python version specified
- [x] Build and start commands defined

## Known Issues

1. **Uvicorn Installation**
   - Issue: `uvicorn` command not found
   - Solution: Ensure virtual environment is activated and dependencies are installed
   - Status: Resolved

2. **File Storage**
   - Issue: Need to ensure uploads directory exists
   - Solution: Added automatic directory creation
   - Status: Resolved

## Testing Checklist

### Before Deployment
- [x] All API endpoints functional
- [x] Error handling working
- [x] File uploads working
- [x] PDF generation working
- [x] Database operations working
- [x] Environment variables configured
- [x] Documentation complete

### After Deployment
- [ ] Verify HTTPS working
- [ ] Test file uploads in production
- [ ] Verify database persistence
- [ ] Check API documentation accessibility
- [ ] Monitor error logs

## Next Steps

1. Implement automated tests
2. Add more comprehensive error handling
3. Set up monitoring and logging
4. Create deployment pipeline
5. Add performance testing 