# Thiis is the main.py file 
from fastapi import FastAPI
from app.config import settings # Importing our application settings
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI(title=settings.app_name)

# Let initialise our first app route 
# Let add template directory 
templates = Jinja2Templates(directory="app/templates")


# Let return our index.html route 
@app.get("/",response_class=HTMLResponse)
async def read_root(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/info")
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

