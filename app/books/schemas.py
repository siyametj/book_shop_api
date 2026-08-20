# app/books/schemas.py

from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., examples=["The python master"])
    author: str = Field(..., examples=["siyam-bro"])
    price: float = Field(..., gt=0, examples=[29.99])
    description: Optional[str] = Field(None, examples=["A awesome book for Python devs!"])

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True

class BookUpdate(BookBase):
    title: Optional[str] = Field(None, examples=["Updated Title"])
    author: Optional[str] = Field(None, examples=['Updated Author'])
    price: Optional[float] = Field(None, gt=0, examples=[35.00])
    description: Optional[str] = Field(None, example=["Updated description"])
