from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, VARCHAR


class System(SQLModel, table=True):
    """
    ## System
    A table of school systems.
    #### Columns
    * id (auto-generated)
    * name (required)
    * state (required)
    * nces_district_id (required)
    * created_at (auto-generated)
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column("name", VARCHAR, unique=True, index=True))
    state: str
    nces_district_id: str
    created_at: datetime = datetime.now()


class SystemInput(SQLModel):
    name: str
    state: str = "AL"
    nces_district_id: str


class SystemOutput(SQLModel):
    id: int
    name: str
    state: str
    nces_district_id: str
    created_at: datetime
