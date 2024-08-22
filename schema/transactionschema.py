import datetime
from pydantic import BaseModel, Field, EmailStr

class Transaction(BaseModel):
    sender_user_id: int = Field(int)
    receiver_user_id:int = Field(int)
    service_type: str = Field(str)
    service_id: str = Field(str)
    amount: float = Field(float)