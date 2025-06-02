from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tinydb import TinyDB, Query
from pathlib import Path

app = FastAPI()
db_path = Path('data/database.json')
db_path.parent.mkdir(exist_ok=True)
db = TinyDB(db_path)

class Item(BaseModel):
    name: str
    description: str | None = None

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    ItemQuery = Query()
    item = db.get(ItemQuery.id == item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    item_dict['id'] = db.insert(item_dict)
    return item_dict
