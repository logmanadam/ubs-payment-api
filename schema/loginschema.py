from pydantic import BaseModel, Field, EmailStr
  
class Login(BaseModel):
    email: EmailStr
    password: str
    