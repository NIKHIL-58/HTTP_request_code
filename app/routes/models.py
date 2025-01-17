from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    id: str = Field(default_factory=ObjectId, alias="_id")
    email: EmailStr
    password: str
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
