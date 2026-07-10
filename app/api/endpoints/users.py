from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate
from app.crud import crud_user
from app.db.database import get_db
from sqlalchemy.orm import Session



router = APIRouter(prefix="/users",tags=["users"])

@router.get("/")
async def get_all_users(db: Session = Depends(get_db)):
    return crud_user.get_all_user(db=db)


@router.get("/{user_id}")
async def get_user_by_id(id:int, db: Session = Depends(get_db)):
    return crud_user.get_user_by_id(db,user_id= id)


@router.post("/")
async def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db,user_create)


@router.delete("/{user_id}")
async def delete_user(id:int,db: Session = Depends(get_db)):
    return crud_user.delete_user(db, user_id = id)


@router.put("/{user_id}")
async def update_user(id: int, user_update: UserCreate,db: Session = Depends(get_db)):
    db_user = crud_user.update_user(db ,user_id = id, user = user_update)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user

