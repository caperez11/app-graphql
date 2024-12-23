from typing import Optional
from sqlmodel import Field, SQLModel
import datetime
import uuid


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str = Field(default_factory=lambda: str(uuid.uuid4()), index=True, nullable=False,
                      unique=True)  # Cambiado a str
    username: str
    email: str
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))
    is_active: bool = Field(default=True)
