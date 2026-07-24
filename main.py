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
    "message": "Student created successfully"},student
    


        
@app.delete("/student/{roll}")
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

@app.get("/students/count")
def countstudents():
    return len(students)

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
























