# Post api call is used to store the data at server side.

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
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

# update the age with respect to name of student
@app.put("/student/{name}")
def update_student(name: str,age:int, student: Student):
    if student_data.get("name") == name:
        student_data["age"] = age  # updating the age in database
        return {"message": "Student data updated successfully", "data": student_data}  # returning the message and updated data
    else:
        raise HTTPException(status_code=404, detail="Student not found")



    
#  HTTP Exception:
