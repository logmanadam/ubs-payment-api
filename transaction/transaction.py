import datetime
from  config.database import get_db
from config.hashing import Hash
from model.walletmodel import Wallets
from schema.transactionschema import Transaction
from model.transectionmodel import Transactions
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session



router = APIRouter(tags= ['Transaction'])

@router.post('/transaction/')
async def wallet_transfer(request: Transaction, db: Session=Depends(get_db)):
    if request.amount < 0 :
        raise HTTPException(status_code=404 , detail="Invalid amount")
    
    sender_wallet = db.query(Wallets).filter(Wallets.user_id == request.sender_user_id).first()
    receiver_wallet = db.query(Wallets).filter(Wallets.user_id == request.receiver_user_id).first()
        
    if not sender_wallet or not receiver_wallet:
        raise HTTPException(status_code=404 , detail="Wallet Not Found")
    if not sender_wallet.balance > request.amount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Insufficient balance")
    
   
    
    sender_wallet.balance -= request.amount
    db.add(sender_wallet)
    db.commit()
     
    receiver_wallet.balance += request.amount
    db.add(receiver_wallet)  
    db.commit()
    
    transaction = Transactions(
        sender_user_id = request.sender_user_id,
        receiver_user_id = request.receiver_user_id,
        service_type = request.service_type,
        service_id = request.service_id,
        amount = request.amount
    )
    db.add(transaction)
    db.commit()
        
    return {
        "message": "Transfer successful",
        "Transaction No": transaction.id,
        "Sender": transaction.sender_user_id,
        "Receiver": transaction.receiver_user_id,
        "Service Type": transaction.service_type,
        "Service ID": transaction.service_id,
        "Amount": transaction.amount
        }
    
@router.get('/transactions/{id}')
async def get_transactions_by_id(id:int,db:Session=Depends(get_db)):
    transaction = db.query(Transactions).filter(Transactions.sender_user_id==id).all()
    return transaction
    
@router.get('/transactions/')
async def transactions(db:Session=Depends(get_db)):
    transactions = db.query(Transactions).all()
    return transactions