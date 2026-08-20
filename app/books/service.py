# app/books/service.py

from sqlalchemy.orm import Session
from app.books.models import BookModel
from app.books.schemas import BookCreate, BookUpdate

class BookService:
    @staticmethod
    def get_all_books(db: Session):
        return db.query(BookModel).all()

    @staticmethod
    def get_book_by_id(db: Session, book_id: int):
        return db.query(BookModel).filter(BookModel.id == book_id).first()

    @staticmethod
    def create_book(db: Session, book_data: BookCreate):
        db_book = BookModel(**book_data.model_dump())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def update_book(db: Session, book_id: int, book_data: BookUpdate):
        db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
        if not db_book:
            return None

        update_data = book_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_book, key, value)

        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def delete_book(db: Session, book_id: int):
        db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
        if not db_book:
            return None
        db.delete(db_book)
        db.commit()
        return True


