from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from schemas.users import User, UserInput, UserOutput

from database import get_session

prefix = "/users"
router = APIRouter(
    prefix=f"{prefix}", tags=[prefix], responses={404: {"description": "Not found."}}
)


@router.get("/", response_model=List[UserOutput])
def get_users(session: Session = Depends(get_session)):
    """Return a list of users."""
    query = select(User)
    return session.exec(query).all()


@router.get("/{id}", response_model=UserOutput)
def get_user_by_id(id: int, session: Session = Depends(get_session)):
    """Return a specified user."""
    user = session.get(User, id)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=404, detail=f"No user with an id of {id} exists."
        )


@router.post("/", response_model=UserOutput)
def add_user(user_input: UserInput, session: Session = Depends(get_session)) -> User:
    """Add a new user"""
    new_user = User(username=user_input.username)
    new_user.set_password(user_input.password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


@router.delete("/{id}", status_code=204)
def delete_user(id: int, session: Session = Depends(get_session)) -> None:
    """Delete a specified user."""
    user = session.get(User, id)
    if user:
        session.delete(user)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"No user with an id of {id} exists."
        )
