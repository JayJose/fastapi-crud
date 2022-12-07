from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from schemas.systems import (
    System,
    SystemInput,
    SystemOutput,
    School,
    SchoolInput,
    SchoolOutput,
)

from database import get_session

prefix = "/systems"
router = APIRouter(
    prefix=f"{prefix}", tags=[prefix], responses={404: {"description": "Not found."}}
)


@router.get("/", response_model=list[SystemOutput])
def get_systems(session: Session = Depends(get_session)) -> SystemOutput:
    """Return a list of systems."""
    query = select(System)
    return session.exec(query).all()


@router.get("/{id}", response_model=SystemOutput)
def get_system_by_id(id: int, session: Session = Depends(get_session)) -> SystemOutput:
    """Return a specified system."""
    system = session.get(System, id)
    if system:
        return system
    else:
        raise HTTPException(
            status_code=404, detail=f"No system with an id of {id} exists."
        )


@router.post("/", response_model=SystemOutput)
def add_system(
    system_input: SystemInput, session: Session = Depends(get_session)
) -> SystemOutput:
    """Add a new system"""
    new_system = System.from_orm(system_input)
    session.add(new_system)
    session.commit()
    session.refresh(new_system)
    return new_system


@router.delete("/{id}", status_code=204)
def delete_system(id: int, session: Session = Depends(get_session)) -> None:
    """Delete a specified system."""
    system = session.get(System, id)
    if system:
        session.delete(system)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"No system with an id of {id} exists."
        )


@router.post("/{system_id}/schools", response_model=School)
def add_school(
    system_id: int, school_input: SchoolInput, session: Session = Depends(get_session)
) -> School:
    system = session.get(System, system_id)
    if system:
        new_school = School.from_orm(school_input, update={"system_id": system_id})
        system.schools.append(new_school)
        session.commit()
        session.refresh(new_school)
        return new_school
    else:
        raise HTTPException(
            status_code=404, detail=f"No system with an id of {id} exists."
        )
