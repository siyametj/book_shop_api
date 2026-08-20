# app/core/deps.py

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import SECRET_KEY, ALGORRITH
from app.users.service import UserService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credits_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials / Token Invalid!",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORRITH])
        email: str = payload.get("sub")
        if email is None:
            raise credits_exception

    except jwt.PyJWTError:
        raise credits_exception

    user = UserService.get_user_by_email(db, email=email)
    if user is None:
        raise credits_exception
    return user
