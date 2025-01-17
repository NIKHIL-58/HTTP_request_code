import os
from dotenv import load_dotenv

load_dotenv()



class Config:
    MONGODB_URI = os.getenv("MONGODB_URI")
    JWT_SECRET = os.getenv("JWT_SECRET")