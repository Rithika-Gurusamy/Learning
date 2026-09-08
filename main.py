from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database import SessionLocal
from models import Student
from sqlalchemy import select


app = FastAPI()




class StudentCreate(BaseModel): 
    name : str
    roll : int
    email : str 
    age : int 

class StudentUpdate(BaseModel):
    name : str | None = None
    age : int | None = None
    email : str | None = None

class Studentresponse(BaseModel):
    name : str
    roll : int
    email : str
    age : int

    model_config = {
        "from_attributes" : True
    }


@app.post("/student")
def create_student(student: StudentCreate):

    with SessionLocal() as session:

        db_student = Student(
            name=student.name,
            roll=student.roll,
            email=student.email,
            age=student.age
        )

        session.add(db_student)

        session.commit()

        return {
            "message": "Student created successfully"
        }

@app.get("/students")
def get_students():

    with SessionLocal() as session:

        stmt = select(Student)

        result = session.execute(stmt)

        students = result.scalars().all()

        return students

@app.get("/students/{roll}")
def get_student_by_roll(roll : int):

    with SessionLocal() as session:

        stmt = select(Student).where(Student.roll == roll)

        result = session.execute(stmt)

        st = result.scalar_one_or_none()
        if st == None:
            raise HTTPException(status_code=404 , detail = "student not found")
        return st
@app.get("/students/email/{email}")
def get_student_by_email(email : str):
    with SessionLocal() as session:
        stmt = select(Student).where(Student.email == email)
        result = session.execute(stmt)
        st = result.scalars().all()
        if len(st) > 0:
            return st
        else:
            raise HTTPException(status_code=404 , detail = "student not found")

@app.patch("/student/update/{roll}",response_model = Studentresponse)
def updatestudent(roll : int ,st : StudentUpdate ):
    with SessionLocal() as session:
        stmt = select(Student).where(Student.roll == roll)
        res = session.execute(stmt)
        s = res.scalar_one_or_none()
        if s == None:
            raise HTTPException(status_code = 404 , detail = "student not found")
        else:
            updatedata = st.model_dump(exclude_unset = True)
            for key,value in updatedata.items():
                setattr(s,key,value)
            session.commit()
            return s 
       
'''
students = []
class studentresponse(BaseModel):
    name : str
    roll : int 

class StudentUpdate(BaseModel):
    name : str | None = None
    age : int | None = None
    email : str | None = None


class Updateemail(BaseModel):
    roll : int
    email : str
{
                
class UpdateAge(BaseModel):
    roll : int
    age : int

class   UpdateName(BaseModel):
    roll : int
    name : str

'''
'''
@app.patch("/update/{roll}")
def updatestudent(roll : int , updates : StudentUpdate):
    for student in students:
        if student.roll == roll:
            updated_data = updates.model_dump(exclude_unset = True)
            for key,value in updated_data.items():
                     setattr(student,key,value)
            return {
                "message" : "student update successfully",
                "student" : student
                                        }
                    
        
        raise HTTPException(status_code =404 , detail = "Student not found")

@app.get("/students")
def get_students():
    return students 

@app.get("/student/{roll}")
def get_onestudent(roll : int ):
    for student in students:
        if student.roll == roll:
            return student
    raise HTTPException(status_code = 404 , detail = "Student not found")

@app.post("/student")
def create_student(student : Student):
    for s in students:
        if s.roll == student.roll:
            raise HTTPException(status_code=400 , detail = "Student already exists")

    students.append(student)
    return {
    "message": "Student created successfully",
    "student": student
    }    


        
@app.delete("/student/roll/{roll}")
def delete_student(roll : int):
    for student in students:
        if student.roll == roll:
            students.remove(student)
            return {
    "message": "Student deleted successfully"}
    raise HTTPException(status_code = 404 , detail="Student not found")



@app.get("/students/count")
def countstudents():
    return {
        "total_students" : len(students)
    }

@app.get("/student/email/{email}")
def get_student_by_email(email : str):
    for s in students:
        if s.email == email:
          return s
    raise HTTPException(status_code= 404 , detail="student not found")

@app.delete("/students")
def deletall():
    students.clear()
    return {
    "message": "All students deleted"
}



@app.get("/students/sorted")
def display():
    sorted_arr = sorted(students,key = lambda st: st.roll)
    return sorted_arr

@app.get("/students/older-than/{age}")
def func(age : int):
    arr = []
    for st in students:
        if st.age > age:
            arr.append(st)
    return arr

@app.get("/students/name/{name}")
def func(name : str):
    arr = []
    for st in students:
        if st.name == name:
            arr.append(st)
    return arr
@app.put("/updateemail")
def updateemail(value : Updateemail):
    for s in students:
        if s.roll == value.roll:
            s.email = value.email
            return {
                "message" : "Student email updated successfully"
            }
    raise HTTPException(status_code= 404 , detail="student not found")
@app.patch("/student/age")
def func(up : UpdateAge):
    for st in students:
        if st.roll == up.roll:
            st.age = up.age
            return {
                "message" : "age updated"
            }
    raise HTTPException(status_code= 404 , detail="student not found")
@app.patch("/student/name")
def func(up : UpdateName):
    for st in students:
        if st.roll == up.roll:
            st.name = up.name
            return {
                "message" : "name updated"
            }
    raise HTTPException(status_code= 404 , detail="student not found")

@app.get("/students/top-oldest")
def get_oldest():
    arr = sorted(students , key = lambda s:s.age)
    if len(arr)> 0:
        return arr[-1]
    return {"message" : "No students are available"}

@app.get("/students/average-age")
def func():
    arr = [st.age for st in students]
    if len(arr) > 0 :
        avg = sum(arr)//len(arr)
        return avg
    return {"message" : "No students are available"}

@app.get("/students/search")
def func(name : str):
    arr = [st for st in students if st.name.lower() == name.lower()]
    return arr


@app.delete("/student/email/{email}")
def get_student_by_email(email : str):
    for student in students:
        if student.email == email:
            students.remove(student)
            return {"message":"student deleted"}
    raise HTTPException(status_code= 404 , detail="student not found") 

@app.put("/student")
def fun(st : Student):
    for i in range(len(students)):
        if students[i].roll == st.roll:
            students[i] = st
            return {
                "message" : "student record updated successfully"

            }

@app.get("/students/rolls")
def fun():
    arr = [st.roll for st in students]
    arr.sort()
    return arr

@app.get("/students/emails")
def fun():
    arr = [st.email for st in students]
    return arr
'''

'''


@app.post("/student") 
def get_student(student : Student): 
    students.append(student) 
    return { 
        "name" : student.name, 
        "roll" : student.roll,
        "email" : student.email, 
        "age" : student.age }



@app.get("/students/{roll}")
def getroll(roll : int):
    return {
        "std _id" : roll
    }

@app.get("/students")
def search(name : str ) :
    return {
        "student_name" : name
    }


@app.get("/books")
def getbook(year : int ):
    return {
    "year": year
}

@app.get("/employees")
def getemployees(limit : int):
    return {
    "limit": limit
}

@app.get("/movies")
def getmovie(genre : str , year : int):
    return {
    "genre" : genre,
    "year": year
}

'''
























