from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tinydb import TinyDB
from pathlib import Path

app = FastAPI()
db_path = Path('data/database.json')
db_path.parent.mkdir(exist_ok=True)
db = TinyDB(db_path)

class Item(BaseModel):
    name: str
    description: str | None = None

@app.get("/items/")
async def read_all_items():
    try:
        items = db.all()
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/items/")
async def create_item(item: Item):
    try:
        item_dict = item.dict(exclude_unset=True)
        db.insert(item_dict)
        return item_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
