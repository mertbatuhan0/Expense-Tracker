from datetime import datetime, timedelta, timezone
from jose import jwt
from decouple import config
from fastapi import status,HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials


SECRET_KEY = config('SECRET_KEY', default='7f8a9b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a')
ALGORITHM = config('ALGORITHM', default='HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = 10

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/Login")
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Payload:", payload)

        user_id = payload.get("user_id")
        print("User ID:", user_id)

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Payload user_id / no sub"
            )
        return user_id
    except Exception as e:
        print("JWT Decode error:", e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token: {str(e)}"
        )

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




