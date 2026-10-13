# Path parameter 
# Inside the URL path itself you can pass the value
from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{product_id}")
def product_detail(product_id: int):
    return f"Product ID: {product_id}"

