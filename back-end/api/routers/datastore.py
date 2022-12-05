from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from sqlalchemy import text

from database import get_session

prefix = "/datastore"
router = APIRouter(
    prefix=f"{prefix}", tags=[prefix], responses={404: {"description": "Not found."}}
)


@router.get("/{table}/data")
def get_data_from_table(table: str, session: Session = Depends(get_session)) -> list:
    """Return data from a specified table."""
    # check if table exists
    # if no table exists raise exception
    sql = text(f"select * from {table}")
    return session.exec(sql).all()


@router.get("{table}/metadata")
def get_metadata_from_table(table: str, session: Session = Depends(get_session)):
    """Return metadata for a specified table."""
    sql = f"""
    SELECT *
    FROM information_schema.columns
    WHERE table_name   = '{table}'
    """
    results = session.exec(sql).all()
    column_names = [_["column_name"] for _ in results]
    table_name = {table}
    return {"table": table_name, "column_names": column_names}
