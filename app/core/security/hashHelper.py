import bcrypt

def hash(password: str) -> str:
    # Şifreyi byte'a çevirip bcrypt ile salt'layarak hash'liyoruz
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_password.decode('utf-8')

def verify(plain_password: str, hashed_password: str) -> bool:
    # Düz şifre ile veritabanındaki hash'i karşılaştırıyoruz
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc, hashed_password_bytes)