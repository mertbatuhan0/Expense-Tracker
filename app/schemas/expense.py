from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    title: str
    amount: int

class ExpenseOut(BaseModel):
    id: int
    title: str
    amount: int

    class Config:
        from_attibutes = True



