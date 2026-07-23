from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

students = [] 
class Student(BaseModel): 
    name : str
    roll : int
    email : str 
    age : int 

@app.post("/student") 
def get_student(student : Student): 
    students.append(student) 
    return { 
        "name" : student.name, 
        "roll" : student.roll,
        "email" : student.email, 
        "age" : student.age }

@app.get("/students")
def get_students(students):
    display_content = ""
    for student in students:

        display_content += student.name + \n 
        display_content += stduent.roll + \n
        display_content += student.email+\n
        display_content += student.age+\n

        
    return display_content 

@app.get("/student/{roll}")
def get_onestudent(roll : int):
    for student in students:
        if student.roll == roll:
            return student
        
@app.put("/strudent/{roll}")
def update_student(roll : int):
    n = int(input("Enter your field"))
    for student in students:
        if student.roll == roll:
            if n == 1:
                name = input("enter name")
                student.name = name
            elif n == 2:
                x = int(input("enter roll number"))
                student.roll = x
            elif n == 3:
                email = input("Enter email")
                student.email = email 
            elif n == 4:
                age = int(input("Enter correct age"))
                student.age = age
    return "Updated successfully"

@app.delete("/student/{roll}")
def delete_student(roll : int):
    for student in students:
        if student.roll == roll:
            students.pop(student)
            return "student deleted succesfully"
'''
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
























