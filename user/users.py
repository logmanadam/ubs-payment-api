from datetime import datetime
from  schema.userschema import User, ShowUser
from  config.database import get_db
from config.hashing import Hash
import model.usermodel as usermodel
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
import stripe


router = APIRouter(tags= ['User'])



@router.post('/user/', response_model = ShowUser)
def create_user(request: User, db: Session=Depends(get_db)):

    new_User = usermodel.Users(
        fullname= request.fullname,
        email=request.email,
        phone_number=request.phone_number,
        password=Hash.bcrypt(request.password),
        creation_date = datetime.utcnow()
        )
    db.add(new_User)
    db.commit()
    db.refresh(new_User)
    return new_User

@router.get('/user/')
def get_user(db: Session=Depends(get_db)):
    users = db.query(usermodel.Users).all()
    return users


stripe.api_key = 'your_stripe_secret_key'

def charge_credit_card(amount, currency, source):
    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=source,
            description="Charge for transfer"
        )
        return charge
    except stripe.error.StripeError as e:
        print(f"Error charging card: {e}")
        return None
