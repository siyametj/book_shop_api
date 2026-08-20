# app/core/security.py

import jwt
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone

pwd_hash = PasswordHash.recommended()

#TODO: THIS come from .env
SECRET_KEY = "supersecretkeythatisatleast32characterlong"
ALGORRITH = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    return pwd_hash.hash(password=password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORRITH)
    return encoded_jwt
