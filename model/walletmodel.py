from datetime import datetime
from config.database import Base
from sqlalchemy import Column, Integer, Float,DateTime

class Wallets(Base):
    __tablename__ = "wallet"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True )
    balance = Column(Float, default= 0.0 )
    creation_date = Column(DateTime, default=datetime.utcnow())
    modified_date = Column(DateTime, nullable=True)