from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

students = [] 
class Student(BaseModel): 
    name : str
    roll : int
    email : str 
    age : int 

class Updateemail(BaseModel):
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

@app.get("/student/{roll}")
def get_onestudent(roll : int):
    for student in students:
        if student.roll == roll:
            return student
    return {
    "message": "Student not found"
}

@app.post("/student")
def create_student(student : Student):
    for s in students:
        if s.roll == student.roll:
            return {
                "message": "Roll number already exists"}

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
    "message": "Student deleted successfully"
}
    return{"message": "Student not found"
    }

@app.put("/emailupdate")
def updateemail(value : Updateemail):
    for s in students:
        if s.roll == value.roll:
            s.email = value.email
            return {
                "message" : "Student email updated successfully"
            }
    return {
    "message": "Student not found"
}

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
    return {
    "message": "Student not found"
}

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
    return {
        "message" : "Student not found"
    } 

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
























