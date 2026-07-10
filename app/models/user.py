from app.db.database import Base
from sqlalchemy import Column, Integer, String,Boolean


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,unique=True)
    mail = Column(String,unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


