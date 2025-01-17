from motor.motor_asyncio import AsyncIOMotorClient
from .config import Config

client = AsyncIOMotorClient(Config.MONGODB_URI)
db = client["user_db"]  # Select or create database
