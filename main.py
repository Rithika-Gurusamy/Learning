from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def fund():
    return "hello"

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
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def func():
    return {
        "message" : "hello"
    }
@app.get("/books/{book_id}")
def fun(book_id):
    return {
        "book_id" : book_id
    }
    '''