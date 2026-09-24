from fastapi import APIRouter,HTTPException,Depends
from database import get_db
from models import Student
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas.student import StudentCreate , StudentUpdate , Studentresponse
from dependencies import get_current_user
from models import User

student_router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@student_router.get("")
def get_students(db:Session = Depends(get_db),current_user : User = Depends(get_current_user)):

    
        stmt = select(Student)
        result = db.execute(stmt)
        students = result.scalars().all()
        ids = []
        for s in students:
            ids.append(s.user_id)
        if current_user.id in ids:
            return students
        else:
            raise HTTPException(status_code = 403 , detail = "you are not authorized to access thisS")

@student_router.get("/email/{email}")
def get_student_by_email(email : str,db:Session = Depends(get_db),current_user : User = Depends(get_current_user)):
    
        stmt = select(Student).where(Student.email == email)
        result = db.execute(stmt)
        st = result.scalars().all()
        if st :
            return st
        elif len(st) <= 0:
            raise HTTPException(status_code=404 , detail = "student not found")
        else:
            raise HTTPException(status_code=403 , detail = "you are not authorized to access this student")

@student_router.post("")
def create_student(student: StudentCreate,db:Session = Depends(get_db),current_user : User = Depends(get_current_user)):
        stmt = select(Student).where(Student.user_id == current_user.id)
        res = db.execute(stmt)
        if res.scalar_one_or_none():
            raise HTTPException(status_code = 409 , detail = "student already exists")
        else:
            db_student = Student(
            name=student.name,
            roll=student.roll,
            email=student.email,
            age=student.age,
            user_id = current_user.id
            )

            db.add(db_student)

            db.commit()

            return {
                "message": "Student created successfully"
            }



@student_router.get("/me")
def get_student(db:Session = Depends(get_db),current_user : User = Depends(get_current_user)):

        stmt = select(Student).where(Student.user_id == current_user.id)
        result = db.execute(stmt)
        st = result.scalar_one_or_none()
        if st:
            return st
        elif st is None:
            raise HTTPException(status_code=404 , detail = "student not found")
        else:
            raise HTTPException(status_code=403 , detail = "you are not authorized to access this student")
       


@student_router.patch("/me",response_model = Studentresponse)
def updatestudent( st : StudentUpdate,db:Session = Depends(get_db),current_user : User = Depends(get_current_user)):
        
        stmt = select(Student).where(Student.user_id == current_user.id)
        res = db.execute(stmt)
        s = res.scalar_one_or_none()
        if s is None:
            raise HTTPException(status_code = 404 , detail = "student not found")
        elif s:
            updatedata = st.model_dump(exclude_unset = True)
            for key,value in updatedata.items():
                setattr(s,key,value)
            db.commit()
            db.refresh(s)
            return s 
        else:
            raise HTTPException(status_code=403 , detail = "you are not authorized to update this student")

@student_router.delete("/me")
def student_delete(db:Session = Depends(get_db),current_user : User = Depends(get_current_user)):
        stmt = select(Student).where(Student.user_id == current_user.id)
        res = db.execute(stmt)
        s = res.scalar().one_or_none()
        if s is None:
            raise HTTPException(status_code=404 , detail = "student not found")
        elif s:
            db.delete(s)
            db.commit()
            return {"message" : "Student deleted successfully"}
        else:
            raise HTTPException(status_code=403 , detail = "you are not authorized to delete this student")
