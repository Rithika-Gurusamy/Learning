from fastapi import APIRouter,HTTPException,Depends
from models import User
from database import get_db
from sqlalchemy import select
from schemas.user import UserCreate
from sqlalchemy.orm import Session
from security import hash_password,verify_password


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@auth_router.post("/signup")
def user_signup(user:UserCreate,db:Session = Depends(get_db)):

    hashed_password = hash_password(user.password)

    new_user = User(

        username = user.username,
        email = user.email,
        hashed_password = hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": f"user {new_user.username} registered successfully"
    }
    
@auth_router.post("/login")
def user_login(user:UserCreate,db:Session = Depends(get_db)):

    n = user.username 
    stmt = select(User).where(User.username == n)
    res = db.execute(stmt)
    us = res.scalar_one_or_none()
    if us == None:
        raise HTTPException(status_code =404 , detail = "user not found")
    else:
        if verify_password(user.password,us.hashed_password):
            return {
                "message" : "user logged in successfully"
            }
        else:
            raise HTTPException(status_code = 401 , detail = "invalid password")
        