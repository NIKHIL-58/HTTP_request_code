from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from .config import Config

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)

