from pydantic import BaseModel, Field, EmailStr
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: EmailStr | None = None