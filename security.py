from pwdlib import PasswordHash
from jose import jwt

SECRET_KEY = "your-super-secret-key"
ALGORITHM = "HS256"


password_hash = PasswordHash.recommended()

def hash_password(password:str):
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str):
    return password_hash.verify(password, hashed_password)

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)