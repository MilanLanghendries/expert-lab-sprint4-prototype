from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

# Create an item
@router.post("/items", response_model=dict)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = models.Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"id": db_item.id, "name": db_item.name, "description": db_item.description, "price": db_item.price}

# Read all items
@router.get("/items", response_model=list[dict])
def read_items(search: str = Query(None), sort: str = Query("id"), db: Session = Depends(database.get_db)):
    query = db.query(models.Item)
    if search:
        query = query.filter((models.Item.name.contains(search)) | (models.Item.description.contains(search)))
    if sort in ["id", "name", "price"]:
        query = query.order_by(sort)
    items = query.all()
    return [{"id": item.id, "name": item.name, "description": item.description, "price": item.price} for item in items]

# Read single item
@router.get("/items/{item_id}", response_model=dict)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item.id, "name": item.name, "description": item.description, "price": item.price}

# Update an item
@router.put("/items/{item_id}", response_model=dict)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.name is not None:
        db_item.name = item.name
    if item.description is not None:
        db_item.description = item.description
    if item.price is not None:
        db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return {"id": db_item.id, "name": db_item.name, "description": db_item.description, "price": db_item.price}

# Delete an item
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}