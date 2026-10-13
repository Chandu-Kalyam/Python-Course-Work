# Post api call is used to store the data at server side.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# class which store the structure of data

class Student(BaseModel):
    name: str
    age: int
    
student_data = {}   # empty dictionary to store the data

@app.post("/student/")
def create_student(student: Student):
    student_data["name"] = student.name  # storing the name in database
    student_data["age"] = student.age     # storing the age in database
    return {"message": "Student data stored successfully", "data": student_data}  # returning the message and data stored in database

