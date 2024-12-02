from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str = None
    price: float

class ItemUpdate(BaseModel):
    name: str = None
    description: str = None
    price: float
