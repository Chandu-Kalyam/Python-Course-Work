# Query Parameter
# Query Parameter is defined by ? in the URL
from fastapi import FastAPI
app = FastAPI()
@app.get("/greet")
def display(name : str = "Guest"):
    return f"Hello: {name}"


