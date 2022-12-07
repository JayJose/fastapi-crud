from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlmodel import Session, select

from schemas.users import User, UserInput, UserOutput
from schemas.tokens import Token, TokenData

from database import get_session

prefix = "/users"
router = APIRouter(
    prefix=f"{prefix}", tags=[prefix], responses={404: {"description": "Not found."}}
)

#### SECURITY
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
SECRET_KEY = "d0c51c14ba233550d76862e4e37ce58aff00de8801ef97af3b30f57c42bb2d5a"  # `openssl rand -hex 32`
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_user(username: str, password: str, session: Session):
    """Verify that the provided password matches the hashed password in the database."""
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Creates an access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    statement = select(User).where(User.username == token_data.username)
    user = session.exec(statement).first()
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Disabled user.")
    return current_user


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


#### END SECURITY


@router.get("/", response_model=list[UserOutput])
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


@router.post("/", response_model=UserOutput, status_code=201)
def add_user(
    user_input: UserInput, session: Session = Depends(get_session)
) -> UserOutput:
    """Add a new user"""
    statement = select(User).where(User.username == user_input.username)
    results = session.exec(statement).first()
    if results:
        raise HTTPException(
            status_code=409,
            detail=f"A user with the username {user_input.username} already exists.",
        )
    else:
        new_user = User(username=user_input.username, disabled=user_input.disabled)
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


@router.get("/me/", response_model=User)
async def get_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


"""
TODO: implement this route
@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
"""
