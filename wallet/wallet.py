from datetime import datetime
from  config.database import get_db
from schema.walletschema import DepositToWallet,AddWallet
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.walletmodel import Wallets
from model.usermodel import Users



router = APIRouter(tags= ['Wallet'])

@router.post('/wallet/')
async def addwallet(request: AddWallet, db: Session=Depends(get_db)):
    newwallet = Wallets(user_id = request.user_id)
    wallet = db.query(Wallets).filter(Wallets.user_id==request.user_id).first()
    user = db.query(Users).filter(Users.id==request.user_id).first()
    if not user:
        raise HTTPException(status_code=404 , detail="User Not Found")
    if not wallet:
        db.add(newwallet)
        db.commit()
        db.refresh(newwallet)
        return {"Your Wallet Number is ": newwallet.id}
    else:
        raise HTTPException(status_code=404 , detail="Your Waller Already Created")
    
    
@router.put('/wallet/deposit/{id}')
def depositmoney(id:int ,request: DepositToWallet , db: Session=Depends(get_db)):
    wallet = db.query(Wallets).filter(Wallets.id==id).first()
    if not wallet:
        raise HTTPException(status_code=404 ,detail="Wallet Not Found")
    if request.amount < 0:
        raise HTTPException(status_code=404 ,detail="Incorrect amount")
    
    wallet.balance +=  float(request.amount)
    wallet.modified_date = datetime.utcnow()
    db.commit()
    db.refresh(wallet)
    return {"You Wallet Balance is" : wallet.balance }

@router.delete('/wallet/{id}')
async def deletewallet(id:int,db:Session=Depends(get_db)):
    wallet = db.query(Wallets).filter(Wallets.id==id).first()
    if not wallet:
        raise HTTPException(status_code=404 ,detail="Wallet Not Found")
    db.delete(wallet)
    db.commit()
    return {"Wallet Deleted"}
    
    
    
@router.get('/wallet/{id}')
def check_balance(id: int, db: Session=Depends(get_db)):
    wallet = db.query(Wallets).filter(Wallets.id==id).first()
    if not wallet:
        raise HTTPException(status_code=404 , detail="Wallet Not Found")
    else:
        return {"You Wallet Balance is" : wallet.balance }
    
    
@router.get('/wallets/')
def show_wallets(db: Session=Depends(get_db)):
    wallet = db.query(Wallets).all()
    if not wallet:
        raise HTTPException(status_code=404 , detail="No Wallets Found")
    else:
        return wallet