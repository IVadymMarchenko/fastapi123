from datetime import date,datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from src.schemas.user import UserResponse


class TodoSchema(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    descriotion: str = Field(min_length=1, max_length=250)
    completed: Optional[bool] = False


class TodoUpdate(TodoSchema):
    completed: bool


class TodoResponse(BaseModel):
    id: int = 1
    title: str
    descriotion: str
    completed: bool
    created_at: datetime | None
    update_at: datetime | None
    user: UserResponse | None

    class Config:
        from_attributes = True
