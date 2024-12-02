from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app import models, schemas, database, security

router = APIRouter()

# Create an item (Requires authentication)
@router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    db_item = models.Item(name=item.name, description=item.description, price=item.price, category=item.category, brand=item.brand)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items", response_model=list[dict])
def read_items(search: str = Query(None), sort: str = Query("id"), db: Session = Depends(database.get_db)):
    query = db.query(models.Item)
    if search:
        query = query.filter((models.Item.name.contains(search)) | (models.Item.description.contains(search)))
    if sort in ["id", "name", "price"]:
        query = query.order_by(sort)
    items = query.all()
    return [
        {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "category": item.category,  
            "brand": item.brand         
        }
        for item in items
    ]

@router.get("/items/{item_id}", response_model=dict)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "id": item.id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "category": item.category,  
        "brand": item.brand         
    }

# Update an item (Requires authentication)
@router.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if item.name:
        db_item.name = item.name
    if item.description:
        db_item.description = item.description
    if item.price:
        db_item.price = item.price
    if item.category:
        db_item.category = item.category
    if item.brand:
        db_item.brand = item.brand

    db.commit()
    db.refresh(db_item)
    return db_item

# Delete an item (Requires authentication)
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}
