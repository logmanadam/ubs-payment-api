from pydantic import BaseModel, Field, EmailStr

class ShowUser(BaseModel):
    fullname: str
    email:  EmailStr
    
    class Config:
        from_attributes = True
        
        
class User(BaseModel):
    fullname: str = Field(str)
    phone_number: int = Field(int,gt=910000000)
    email: EmailStr = Field(str)
    password: str = Field(str, min_length=8)
