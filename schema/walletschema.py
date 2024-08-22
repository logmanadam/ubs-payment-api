import datetime
from pydantic import BaseModel, Field, EmailStr

class Wallet(BaseModel):
    user_id: int = Field(int)
    balance: float = Field(float)
    
class AddWallet(BaseModel):
    user_id: int = Field(int)
class DepositToWallet(BaseModel):
    amount: float 