from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, VARCHAR


class School(SQLModel, table=True):
    """
    ## School
    A table of schools.
    #### Columns
    * id (auto-generated)
    * name (required)
    * system_id (required)
    * created_at (auto-generated)
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column("name", VARCHAR, unique=True, index=True))
    system_id: int
    created_at: datetime = datetime.now()


class SchoolInput(SQLModel):
    name: str
    system_id: int


class SchoolOutput(SQLModel):
    id: int
    name: str
    system_id: int
    created_at: datetime
