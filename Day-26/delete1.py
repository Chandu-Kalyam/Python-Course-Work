from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool


item_db = {
    1: {"name": "Laptop", "price": 1000, "is_offer": False},
    2: {"name": "Phone", "price": 500, "is_offer": True},
    3: {"name": "Tablet", "price": 300, "is_offer": False},
}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in item_db:
        deleted_item = item_db[item_id]
        del item_db[item_id]
        return {"message": f"Item with ID {item_id} deleted successfully.", "deleted_item": deleted_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.post("/items/")
def create_item(item: Item):
    item_id = max(item_db.keys()) + 1 if item_db else 1
    item_db[item_id] = item.dict()
    
    return {"message": f"Item created successfully.", "item": item_db[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in item_db:
        item_db[item_id] = item.dict()
        return {"message": f"Item with ID {item_id} updated successfully.", "item": item_db[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in item_db:
        return {"item": item_db[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# put, get, post.

#logging: Debug, info, warning, error, critical