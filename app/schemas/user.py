from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    mail: str
    hashed_password: str



