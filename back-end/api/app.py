from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from database import engine
from routers import root, users, systems
from config import settings

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
)

prefix = settings.API_PREFIX
app.include_router(root.router, prefix=prefix)
app.include_router(users.router, prefix=prefix)
app.include_router(systems.router, prefix=prefix)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
