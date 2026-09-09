from fastapi import APIRouter,HTTPException,Depends
from database import get_db
from models import Student
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas.student import StudentCreate , StudentUpdate , Studentresponse

student_router = APIRouter()



@student_router.post("/student")
def create_student(student: StudentCreate,db:Session = Depends(get_db)):

    
        db_student = Student(
            name=student.name,
            roll=student.roll,
            email=student.email,
            age=student.age
        )

        db.add(db_student)

        db.commit()

        return {
            "message": "Student created successfully"
        }

@student_router.get("/students")
def get_students(db:Session = Depends(get_db)):

    
        stmt = select(Student)

        result = db.execute(stmt)

        students = result.scalars().all()

        return students

@student_router.get("/students/{roll}")
def get_student_by_roll(roll : int,db:Session = Depends(get_db)):

        stmt = select(Student).where(Student.roll == roll)

        result = db.execute(stmt)

        st = result.scalar_one_or_none()
        if st == None:
            raise HTTPException(status_code=404 , detail = "student not found")
        return st

@student_router.get("/students/email/{email}")
def get_student_by_email(email : str,db:Session = Depends(get_db)):
    
        stmt = select(Student).where(Student.email == email)
        result = db.execute(stmt)
        st = result.scalars().all()
        if len(st) > 0:
            return st
        else:
            raise HTTPException(status_code=404 , detail = "student not found")

@student_router.patch("/student/update/{roll}",response_model = Studentresponse)
def updatestudent(roll : int ,st : StudentUpdate,db:Session = Depends(get_db)):
        
        stmt = select(Student).where(Student.roll == roll)
        res = db.execute(stmt)
        s = res.scalar_one_or_none()
        if s == None:
            raise HTTPException(status_code = 404 , detail = "student not found")
        else:
            updatedata = st.model_dump(exclude_unset = True)
            for key,value in updatedata.items():
                setattr(s,key,value)
            db.commit()
            db.refresh(s)
            return s 
@student_router.delete("/student/delete/{roll}")
def student_delete(roll : int , db:Session = Depends(get_db)):
        stmt = select(Student).where(Student.roll == roll)
        res = db.execute(stmt)
        s = res.scalar_one_or_none()
        if s == None:
            raise HTTPException(status_code=404 , detail = "student not found")
        else:
            db.delete(s)
            db.commit()
            return {"message" : "Student deleted successfully"}