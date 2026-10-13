# get API call
from fastapi import FastAPI
# protocol:domain:portnumber/path?query parameter
# http://127.0.0.1:8000/Home?name=vicky&age=20
# Create an object for using FastAPI
app = FastAPI()

# @decorator to make get API call
@app.get("/")
def dashboard():
    return "Welcome to the FastAPI dashboard!"

@app.get("/Home")
def Home():
    return "Welcome to Home Page"

@app.get("/student/marks")
def stu():
    return "My marks is 100"

