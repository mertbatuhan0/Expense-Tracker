from fastapi import FastAPI
from app.api.endpoints import expenses
from app.api.endpoints import users
from app.db.database import engine, Base

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(expenses.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {" welcome to Expenses-Tracker"}