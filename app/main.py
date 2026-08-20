from fastapi import FastAPI

from app.database import engine, Base
from app.books.models import BookModel
from app.users.models import UserModel

from app.books.router import router as books_router
from app.users.router import router as auth_router


# Create database tables
Base.metadata.create_all(bind=engine)


# FastAPI application
app = FastAPI(
    title="Book Shop API",
    description="My first book shop API project",
    version="1.0.1"
)


# Routers
app.include_router(books_router)
app.include_router(auth_router)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Book Shop API"
    }
