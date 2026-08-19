from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = []

class StudentUpdate(BaseModel):
    name : str|None = None
    age : int|None = None
    email : str|None = None
    
class Student(BaseModel):
    name : str
    roll : int
    email : str
    age : int

class StudentResponse(BaseModel):
    name: str
    roll: int
    email: str

@app.post("/students",status_code=201)
def create_student(s : Student):
    for st in students:
        if st.roll == s.roll:
            raise HTTPException(status_code=400 , detail = "Student already exists")
    students.append(s)
    return {
        "message" : "student created successfully"
    }


@app.get("/students/search")
def get_student_name(name : str):
    res = []
    for s in students:
        if s.name.lower() == name.lower():
            res.append(s)
    return res
            

@app.get("/students/{roll}",response_model=StudentResponse)
def get_student(roll : int ):
    for s in students:
        if s.roll == roll:
            return s
    raise HTTPException(status_code=404,detail="student not found")

@app.patch("/students/{roll}")
def update_student(roll : int , input : StudentUpdate):
    for s in students:
        if s.roll == roll:
            data = input.model_dump(exclude_unset=True)
            for k,v in data.items():
                setattr(s,k,v)
            return {
                "message" : "student updates successfully"
            }
    raise HTTPException(status_code=404 , detail ="student not found")


@app.delete("/students/{roll}")
def delete_student(roll : int):
    for s in students:
        if s.roll == roll:
            students.remove(s)
            return {
                "message" : "student deleted successfully"
            }
    raise HTTPException(status_code=404 , detail= "Student not found")
































'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []
class Student(BaseModel):
    roll : int
    name : str
    email : str
    mobile : int
    age : int 

class UpdateEmail(BaseModel):
    roll : int
    email : str

class UpdateAge(BaseModel):
    roll : int
    age : int

class   UpdateName(BaseModel):
    roll : int
    name : str

@app.get("/students")
def get_students():
    return students

@app.post("/student")
def create_student(student : Student):
    
    for st in students:
        if st.roll == student.roll:
            return {
                "message" : "student already exists"
            }
        if st.email == student.email:
            return {
                "message" : "email already exists , try again"
            }
    if student.age < 1 :
        return {
            "message" : "age is less than 1 "
        }
    if student.name.strip() == "":
        return {
            "message" : "enter valid name"
        }
    students.append(student)
    return {
        "message" : "student added successfully"
    }

@app.get("/student/roll/{roll}")
def get_one_student(roll : int):
    for student in students:
        if student.roll == roll:
            return {"message":"student exists"},student
    return {
        "message" : "Student not found"
    }

@app.delete("/delete/student/{roll}")
def delete_stduent(roll : int):
    for i in range(len(students)):
        if students[i].roll == roll:
            students.remove(students[i])
            return {
                "message" : "student deleted successfully"
                                        }
    return {
        "message" :"student not found"
    }

@app.patch("/emailupdate")
def update_email(em : UpdateEmail):
    for st in students:
        if st.roll == em.roll:
            st.email = em.email
            return {
                "message" : "student email updated"
            }

@app.get("/students/count")
def count():
    x = len(students)
    return {
        "message" : f"The total students {x}" }

@app.get("/student/email/{email}")
def get_student_by_email(email : str):
    for student in students:
        if student.email == email:
            return {"message":"student exists"},student
    return {
        "message" : "Student not found"
    } 

@app.delete("/students")
def del_students():
    students.clear()
    return {
        "message" : "all students deleted"
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

@app.patch("/student/age")
def func(up : UpdateAge):
    for st in students:
        if st.roll == up.roll:
            st.age = up.age
            return {
                "message" : "age updated"
            }
    return {
        "message" : "student not found"
    }

@app.patch("/student/name")
def func(up : UpdateName):
    for st in students:
        if st.roll == up.roll:
            st.name = up.name
            return {
                "message" : "name updated"
            }
    return {
        "message" : "student not found"
    }

@app.get("/students/top-oldest")
def get_oldest():
    arr = sorted(students , key = lambda s:s.age)
    if len(arr) > 0:
        return arr[-1]
    return {
            "message" : "student not found"
        }

@app.get("/students/average-age")
def func():
    arr = [st.age for st in students]
    if len(arr) > 0:
        avg = sum(arr)//len(arr)
        return avg
    return {
            "message" : "student not found"
        }

@app.get("/students/search")
def func(name : str):
    arr = [st for st in students if st.name.lower() == name.lower()]
    return arr


@app.delete("/student/{email}")
def get_student_by_email(email : str):
    for student in students:
        if student.email == email:
            students.remove(student)
            return {"message":"student deleted"}
    return {
        "message" : "Student not found"
    } 

@app.put("/student")
def fun(st : Student):
    for i in range(len(students)):
        if students[i].roll == st.roll:
            students[i ] = st
            return {
                "message" : "student record updated successfully"

            }
    return {
        "message" : "student not found"
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