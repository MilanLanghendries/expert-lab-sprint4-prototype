from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

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

class Item(BaseModel):  
    id: int
    name: str
    description: str
    price: float
    category: str
    brand: str

    class Config:
        orm_mode = True  