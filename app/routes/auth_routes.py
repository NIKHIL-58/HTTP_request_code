from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pymongo.errors import DuplicateKeyError
from datetime import timedelta
from .database import db
from jose import jwt
from .models import UserModel
from pydantic import BaseModel, EmailStr
from .schemas import UserCreate, UserLogin
from .auth import hash_password, verify_password, create_access_token

router = APIRouter()




class Config:
    JWT_SECRET = "your_secret_key_here"  
    JWT_ALGORITHM = "HS256"


def create_access_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)

@router.post("/register")
async def register(user: UserCreate):
    # Check if user already exists
    user_exists = await db["users"].find_one({"email": user.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_pw = hash_password(user.password)
    
    # Create the user dictionary with username, mobile, email, and password
    user_dict = {
        "username": user.username,
        "mobile": user.mobile,
        "email": user.email,
        "password": hashed_pw
    }
    
    # Insert the user into the database
    await db["users"].insert_one(user_dict)
    
    return {"message": "User registered successfully"}


@router.post("/login")
async def login(user: UserLogin):
    # Check if the user exists in the database
    db_user = await db["users"].find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate a JWT token with the user's email as the subject
    access_token = create_access_token(data={"sub": db_user["email"]})
    
    # Respond with the token and a success message
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message": "User login successfully"
    }




