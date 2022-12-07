from datetime import datetime
from passlib.context import CryptContext
from sqlmodel import SQLModel, Field, Relationship, Column, VARCHAR

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(SQLModel, table=True):
    """
    ## Users
    A table of users.
    #### Columns
    * id
    * password_hash
    * disabled (default: False)
    * created_at
    """

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(
        sa_column=Column("username", VARCHAR, unique=True, index=True)
    )
    password_hash: str
    disabled: bool
    created_at: datetime = datetime.now()

    def set_password(self, password):
        """Set the hashed password."""
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        """Verify the hashed password."""
        return pwd_context.verify(password, self.password_hash)


class UserInput(SQLModel):
    username: str
    password: str
    disabled: bool = False


class UserOutput(SQLModel):
    id: int
    username: str
    disabled: bool
    created_at: datetime
