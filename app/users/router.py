# app/users/router.py

from app.database import get_db
from sqlalchemy.orm import Session
from app.users.service import UserService
from app.core.security import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from app.users.schemas import UserCreate, UserResponse
from fastapi import APIRouter, HTTPException, status, Depends

router = APIRouter(
    prefix="/auth",
    tags=["Authentication & Users"]
)

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = UserService.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered! Try logging in."
        )
    return UserService.create_user(db, user)

@router.post("/login")
def login_user(
    from_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = UserService.authenticate_user(db, from_data.username, from_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token = create_access_token(data={"sub": user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
