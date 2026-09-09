from pydantic import BaseModel


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
