from fastapi_offline import FastAPIOffline
from fastapi import FastAPI
from auth import authentications
from config.database import get_db, engine
import model.usermodel as usermodel
from wallet import wallet
from user import users
from transaction import transaction

app = FastAPIOffline()

usermodel.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(wallet.router)
app.include_router(transaction.router)
app.include_router(authentications.router)