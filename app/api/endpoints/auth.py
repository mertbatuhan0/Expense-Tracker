from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from app.schemas .user import UserInLogin,UserCreate
from app.models.user import User
from app.core.security.hashHelper import verify
from app.core.security import authHandler, hashHelper
from app.db.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/Login")
async def login(user_credentials:UserInLogin, db: Session = Depends(get_db)):
   user = db.query(User).filter(User.mail == user_credentials.mail).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credentials")

   if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")

   access_token  = authHandler.create_access_token(data={"user_id":user.id})
   return {"access_token":access_token, "token_type":"bearer"}


@router.post("/Signup")
async def signup(user_signup: UserCreate, db: Session = Depends(get_db)):
   hashed_password = hashHelper.hash(user_signup.password)
   new_user = User(mail=user_signup.mail,username=user_signup.username,password=hashed_password)
   db.add(new_user)
   existing_user = db.query(User).filter(User.mail == user_signup.mail).first()
   if existing_user:
      raise HTTPException(status_code=400, detail="User already exists")

   db.commit()
   db.refresh(new_user)
   return new_user

