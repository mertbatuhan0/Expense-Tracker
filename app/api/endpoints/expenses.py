from typing import List, Optional
from unittest import skip

import optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.expense import ExpenseCreate, ExpenseOut
from app.crud import crud_expense
from app.core.security.authHandler import get_current_user

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.get("/", response_model=List[ExpenseOut])
async def get_all_expenses(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 5,
        max_value: Optional[int] = None,
        min_value: Optional[int] = None,
        title: Optional[str] = None,
        current_user_id: str = Depends(get_current_user)
):
    return crud_expense.get_all_expenses(db=db, user_id=current_user_id, skip=skip, limit=limit, max_value=max_value, min_value=min_value, title=title)


@router.get("/{id}", response_model=ExpenseOut)
async def get_expenses_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    expense = crud_expense.get_expense_by_id(db=db, expense_id=id, user_id=current_user_id)
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    return expense


@router.post("/", response_model=ExpenseOut)
async def create_expense(
    expense_create: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    return crud_expense.create_expense(
        db=db,
        expense=expense_create, 
        user_id=current_user_id
    )


@router.delete("/{id}", response_model=ExpenseOut)
async def delete_expenses(
    id: int,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    return crud_expense.delete_expense(db=db, expense_id=id, user_id=current_user_id)


@router.put("/{id}", response_model=ExpenseOut)
async def update_expenses(
    id: int,
    expense_update: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    updated_expense = crud_expense.update_expense(
        db=db,
        expense_id=id,
        expense_update=expense_update,
        user_id=current_user_id
    )

    if not updated_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found or unauthorized")

    return updated_expense


