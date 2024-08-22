from datetime import datetime
from config.database import Base
from sqlalchemy import Column, Integer, Float,String,DateTime


class Transactions(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    service_type  = Column(String, nullable=True)
    sender_user_id = Column(Integer, index=True)
    receiver_user_id = Column(Integer, index=True)
    service_id  = Column(String,nullable=True)
    amount = Column(Float)
    fee = Column(Float, default= 1.5)
    creation_date = Column(DateTime, default=datetime.utcnow())