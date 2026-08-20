# app/users/service.py

from sqlalchemy.orm import Session
from app.users.models import UserModel
from app.users.schemas import UserCreate
from app.core.security import hash_password, verify_password

class UserService:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        hashed_pwd = hash_password(user_data.password)
        db_user = UserModel(email=user_data.email, hashed_password=hashed_pwd)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(UserModel).filter(UserModel.email == email).first()

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):
        user = UserService.get_user_by_email(db, email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

