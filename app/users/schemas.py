# app/users/schemas.py

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr = Field(..., examples=["user@gmail.com"])
    password: str = Field(..., min_length=8, examples=['12345678'])

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
