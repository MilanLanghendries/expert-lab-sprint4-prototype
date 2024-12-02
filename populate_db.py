from sqlalchemy.orm import Session
from app.models import Item
from app.database import engine

# Create initial data
initial_data = [
    {"name": "Laptop", "description": "A high-performance laptop", "price": 999.99},
    {"name": "Smartphone", "description": "Latest model smartphone", "price": 699.99},
    {"name": "Headphones", "description": "Noise-cancelling headphones", "price": 199.99},
    {"name": "Monitor", "description": "4K Ultra HD monitor", "price": 299.99},
    {"name": "Keyboard", "description": "Mechanical keyboard", "price": 89.99},
]

# Populate the database
def populate_database():
    with Session(engine) as session:
        for item in initial_data:
            db_item = Item(name=item["name"], description=item["description"], price=item["price"])
            session.add(db_item)
        session.commit()
        print("Database populated successfully!")

if __name__ == "__main__":
    populate_database()
