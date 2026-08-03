from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate

def get_all_expenses(
        db: Session,
        user_id: str,
        skip: int = 0,
        limit: int = 5,
        max_value: Optional[int] = None,
        min_value: Optional[int]= None,
        title: Optional[str] = None):
    query = db.query(Expense).filter(Expense.user_id == user_id)

    if min_value is not None:
        query = query.filter(Expense.amount >= min_value)

    if max_value is not None:
        query = query.filter(Expense.amount <= max_value)

    if title is not None:
        query = query.filter(Expense.title == title)

    return query.offset(skip).limit(limit).all()


def get_expense_by_id(db: Session, expense_id: int, user_id: str):
    return db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user_id).first()


def create_expense(db: Session, expense: ExpenseCreate, user_id: str):
        db_expense = Expense(
            title=expense.title,
            amount=expense.amount,
            user_id=user_id
        )
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        return db_expense

def delete_expense(db: Session, expense_id: int, user_id: str):
    del_expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user_id).first()

    if not del_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found or unauthorized")

    db.delete(del_expense)
    db.commit()
    return del_expense

def update_expense(db: Session, expense_id: int, expense_update: ExpenseCreate, user_id: str):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user_id).first()

    if not expense:
        return None

    expense.title = expense_update.title
    expense.amount = expense_update.amount

    db.commit()
    db.refresh(expense)
    return expense