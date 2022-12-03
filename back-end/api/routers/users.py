from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from schemas.users import User, UserInput

from database import get_session

prefix = "/users"
router = APIRouter(
    prefix=f"{prefix}", tags=[prefix], responses={404: {"description": "Not found"}}
)


@router.get("/")
def get_users(session: Session = Depends(get_session)):
    """Return a list of users."""
    query = select(User)
    return session.exec(query).all()


@router.get("/{id}", response_model=User)
def get_user_by_id(id: int, session: Session = Depends(get_session)):
    """Return a specific user."""
    user = session.get(User, id)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=404, detail=f"No user with an id of {id} exists."
        )


@router.post("/", response_model=User)
def add_user(user_input: UserInput, session: Session = Depends(get_session)) -> User:
    new_user = User.from_orm(user_input)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
