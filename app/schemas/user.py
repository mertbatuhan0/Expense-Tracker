from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    mail: str
    password: str

class UserOut(UserCreate):
    username: str
    email: str

    class Config:
        from_attibutes = True

class UserUpdate(BaseModel):
    username: str
    mail: str
    email: str
    password: str


class UserInLogin(BaseModel):
    mail: str
    password: str

class UserWithToken(BaseModel):
    token: str






