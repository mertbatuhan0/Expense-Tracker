from sqlalchemy.sql.schema import ForeignKey

from app.db.database import Base
from sqlalchemy import Column, Integer,String

#we are using models for database tables

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True)
    amount = Column(Integer,index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

