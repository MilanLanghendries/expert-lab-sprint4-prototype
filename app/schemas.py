from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str  
    brand: str     

class ItemUpdate(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    category: str = None  
    brand: str = None     
