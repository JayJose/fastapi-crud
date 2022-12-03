from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from schemas.schools import School, SchoolInput, SchoolOutput

from database import get_session

prefix = "/schools"
router = APIRouter(
    prefix=f"{prefix}", tags=[prefix], responses={404: {"description": "Not found."}}
)


@router.get("/", response_model=List[SchoolOutput])
def get_schools(session: Session = Depends(get_session)) -> SchoolOutput:
    """Return a list of schools."""
    query = select(School)
    return session.exec(query).all()


@router.get("/{id}", response_model=SchoolOutput)
def get_school_by_id(id: int, session: Session = Depends(get_session)) -> SchoolOutput:
    """Return a specified school."""
    school = session.get(School, id)
    if school:
        return school
    else:
        raise HTTPException(
            status_code=404, detail=f"No school with an id of {id} exists."
        )


@router.post("/", response_model=SchoolOutput)
def add_school(
    input: SchoolInput, session: Session = Depends(get_session)
) -> SchoolOutput:
    """Add a new school"""
    new_data = School.from_orm(input)
    session.add(new_data)
    session.commit()
    session.refresh(new_data)
    return new_data


@router.delete("/{id}", status_code=204)
def delete_school(id: int, session: Session = Depends(get_session)) -> None:
    """Delete a specified school."""
    school = session.get(School, id)
    if school:
        session.delete(school)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"No school with an id of {id} exists."
        )
