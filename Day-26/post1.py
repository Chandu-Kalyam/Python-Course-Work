from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# defining the datatype in which data must be recieve

class Student(BaseModel):
    name: str
    age: int
    
    
@app.post("/students/")
def create_student(student: Student):
    return {"name": student.name, "age": student.age}
    

