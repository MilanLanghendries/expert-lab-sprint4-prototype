from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'  # Table name in the database

    # Columns of the 'items' table
    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key column
    name = Column(String, nullable=False)  # Name of the item (required field)
    description = Column(String, nullable=True)  # Description of the item
    price = Column(Float, nullable=False)  # Price of the item
    category = Column(String, nullable=True)  # Category of the item
    brand = Column(String, nullable=True)  # Brand of the item

    # Optional: Add a __repr__ method to improve object representation
    def __repr__(self):
        return f"<Item(name={self.name}, category={self.category}, brand={self.brand}, price={self.price})>"
