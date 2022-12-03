from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

# need to import models before calling create_all
from schemas import users

from database import engine
import routers.root
import routers.users
from config import settings

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


prefix = settings.API_PREFIX

app.include_router(routers.root.router, prefix=prefix)
app.include_router(routers.users.router, prefix=prefix)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
