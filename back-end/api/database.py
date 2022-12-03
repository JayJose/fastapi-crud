from sqlmodel import create_engine, Session

from config import settings

user = settings.POSTGRES_USER
password = settings.POSTGRES_PASSWORD

host = settings.POSTGRES_HOST
db = settings.POSTGRES_DB
port = settings.POSTGRES_PORT


POSTGRES_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"
print(POSTGRES_URL)
engine = create_engine(POSTGRES_URL, echo=True)  # log the generated SQL


def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
