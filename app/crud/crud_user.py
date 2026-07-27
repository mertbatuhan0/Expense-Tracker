from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from fastapi import HTTPException


def get_all_user(db:Session):
    get_users = db.query(User).all()
    return get_users


def get_user_by_id(db:Session, user_id:int):
    get_user = db.query(User).filter(User.id == user_id).first()
    return get_user


def create_user(db:Session, user: UserCreate):
    db_user = User(username=user.username, mail=user.mail, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db:Session, user_id: int):
    deleted_user = db.query(User).filter(User.id == user_id).first()

    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(deleted_user)
    db.commit()
    return deleted_user

def update_user(db:Session,user_id:int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user:
        db_user.username = user.username
        db_user.mail = user.mail
        db_user.password = HashHelper.hash_password(user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    raise HTTPException(status_code=404, detail="User not found")
