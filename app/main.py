# Thiis is the main.py file 
from fastapi import FastAPI
from app.config import settings # Importing our application settings

app = FastAPI(title=settings.app_name)

# Let initialise our first app route 

@app.get("/")
async def root():
    return{
        "message":"Welcome to My System Health Dashboard for CodingAtom",
        "app_name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "Status": "Online"
    }

@app.get('/health')
async def health_check():
    return{
        "status":"healthy","version":settings.app_version
    }