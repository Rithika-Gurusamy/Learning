from fastapi import APIRouter,HTTPException,Depends
from models import User
from database import get_db
from sqlalchemy import select
from schemas.user import UserCreate,Userlogin
from sqlalchemy.orm import Session
from security import hash_password,verify_password,create_access_token
from fastapi.security import OAuth2PasswordRequestForm

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
        hashed_password = hashed_password,
        role = user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": f"user {new_user.username} registered successfully"
    }
    
@auth_router.post("/login")
def user_login(user:Userlogin,db:Session = Depends(get_db)):

    n = user.username 
    stmt = select(User).where(User.username == n)
    res = db.execute(stmt)
    us = res.scalar_one_or_none()
    if us == None:
        raise HTTPException(status_code =404 , detail = "user not found")
    else:
        if verify_password(user.password,us.hashed_password) and user.role == us.role:
            access_token = create_access_token({
                "sub" : str(us.id),
                "role" : str(us.role)
            })

            return {
                "message" : "user logged in successfully",
                "access_token" : access_token,
                "token_type" : "bearer"
            }
        else:
            raise HTTPException(status_code = 401 , detail = "invalid credentials")
        
