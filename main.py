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