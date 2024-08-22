from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from  config.database import get_db
from config.hashing import Hash
from  schema.tokenschema import Token
from  schema.loginschema import Login
from config.JWToken import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
import model.usermodel as usermodel




router = APIRouter(tags=['Authentication'])

@router.post('/auth/')
def login(request: Login, db: Session=Depends(get_db)):
    user = db.query(usermodel.Users).filter(usermodel.Users.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credential")
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=404, detail="Invalid Password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")