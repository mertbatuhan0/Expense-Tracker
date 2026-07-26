from bcrypt import checkpw, hashpw, gensalt


class HashHelper:

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode("utf-8")
        try:
            return checkpw(plain_password.encode("utf-8"), hashed_password)
        except ValueError:

            return False

    @staticmethod
    def hash_password(plain_password: str) -> str:
        pwd_bytes = plain_password.encode("utf-8")
        salt = gensalt()
        return hashpw(pwd_bytes, salt).decode("utf-8")