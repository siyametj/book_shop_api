# app/books/models.py

from app.database import Base
from sqlalchemy import Column, Integer, String, Float

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)

