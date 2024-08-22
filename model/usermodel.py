from datetime import datetime
from config.database import Base
from sqlalchemy import Column, Integer, String,Boolean,DateTime
from sqlalchemy.orm import relationship
from model.walletmodel import Wallets

class Users(Base):
    
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    phone_number = Column(Integer)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean,default=True)
    creation_date = Column(DateTime, default=datetime.utcnow())
    modified_date = Column(DateTime,nullable=True)