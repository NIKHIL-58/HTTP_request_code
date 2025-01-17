from pydantic import BaseModel, EmailStr, root_validator
from passlib.context import CryptContext

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    username: str
    mobile: str
    email: EmailStr
    password: str

    @root_validator(pre=True)
    def check_passwords_match(cls, values):
        password = values.get('password')
        return values

    def hash_password(self):
        """Hashes the password using bcrypt."""
        return pwd_context.hash(self.password)


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class MyModel(BaseModel):
    class Config:
        populate_by_name = True 