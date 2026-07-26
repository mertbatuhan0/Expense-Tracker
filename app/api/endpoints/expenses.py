from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_expense
from app.db.database import get_db
from app.schemas.expense import ExpenseCreate, ExpenseOut


router = APIRouter(prefix="/expenses",tags=["expenses"])


#response_model=UserOut sayesinde FastAPI bu nesneyi alıp UserOut'a göre süzüyor — client sadece id, username, mail görüyor.

@router.get("/",response_model=list[ExpenseOut])
async def get_all_expenses(db: Session = Depends(get_db)):
    return crud_expense.get_all_expenses(db)


@router.get("/{id}",response_model=ExpenseOut)
async def get_expenses_by_id(db: Session = Depends(get_db), id: int=None):
    return crud_expense.get_expense_by_id(db,expense_id = id)
#we don't use depends(get_db) in endpoints just use cruds

@router.post("/",response_model=ExpenseOut)
async def create_expense(expense_create:ExpenseCreate, db: Session = Depends(get_db)):
    return crud_expense.create_expense(db,expense_create)


@router.delete("/{id}",response_model=ExpenseOut)
async def delete_expenses(db: Session = Depends(get_db),id: int=None):
   return crud_expense.delete_expense(db,expense_id=id)


@router.put("/{id}",response_model=ExpenseOut)
async def update_expenses(id: int, expense_update: ExpenseCreate, db: Session = Depends(get_db)):
    updated_expense = crud_expense.update_expense(db, expense_id=id, expense_update=expense_update)

    if not updated_expense:
        raise HTTPException(status_code=404, detail="Expense not found.")
    return updated_expense


