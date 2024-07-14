from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users
from .database import engine
from .models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_credentials=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/status")
def get_status():
    return {"status": "running"}

app.include_router(users.router, prefix="/users")