from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crime.routes import router
from config import settings

app = FastAPI(
    title="An API title",
    description="An API description",
    version="An API version",
)

prefix = "prefix"

app.include_router(router)
app.include_router(router, prefix=prefix)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
