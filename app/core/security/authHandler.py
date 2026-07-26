import jwt
from decouple import config
import time


SECRET_KEY = config('SECRET_KEY', default='super_secret_key_123456')
ALGORITHM = config('ALGORITHM', default='HS256')


class AuthHandler:

 @staticmethod
 def decode_jwt(token):
    try:
        decoded_token = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decoded_token if decoded_token['expiration'] > time.time() else None
    except:
        print("Error decoding jwt token")


def sign_jwt(user_id):
    payload = { "user_id": user_id,"expiration": time.time() + 900}
    token = jwt.encode(payload,algorithm=ALGORITHM)
    return token












