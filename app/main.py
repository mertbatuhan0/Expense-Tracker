from fastapi import FastAPI
from app.api.endpoints import expenses, users, auth
from app.db.database import engine, Base
import app.models

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(expenses.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {" welcome to Expenses-Tracker"}