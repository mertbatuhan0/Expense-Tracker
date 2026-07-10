from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate
from fastapi import HTTPException,status

def get_all_expenses(db:Session):
    get_expenses = db.query(Expense).all()
    return get_expenses


def get_expense_by_id(db:Session, expense_id: int,):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    db.refresh(expense)
    return expense


def create_expense(db:Session, expense_create = ExpenseCreate):
    new_expense = Expense(title=expense_create.title,amount=expense_create.amount)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

def delete_expense(db:Session, expense_id: int):
    del_expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not del_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Expense not found")

    db.delete(del_expense)
    db.commit()
    db.refresh(del_expense)
    return del_expense


def update_expense(db:Session, expense_id :int ,expense_update: ExpenseCreate):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if expense:
        expense.title = expense_update.title
        expense.amount = expense_update.amount
        db.add(expense)
        db.commit()
        db.refresh(expense)
    return expense