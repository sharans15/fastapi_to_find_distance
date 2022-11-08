from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum as Enum_, IntEnum

from models.user_models import User

class Gem(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    location: str
    distance: Optional[float]
    
    




    