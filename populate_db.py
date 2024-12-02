from sqlalchemy.orm import Session
from app.models import Item, Base
from app.database import engine

# Create initial data with 50+ items
initial_data = [
    {"name": "iPhone 12", "category": "Smartphone", "brand": "Apple", "description": "Latest iPhone model", "price": 799.99},
    {"name": "iPhone 13", "category": "Smartphone", "brand": "Apple", "description": "Latest iPhone model", "price": 899.99},
    {"name": "Samsung Galaxy S21", "category": "Smartphone", "brand": "Samsung", "description": "Flagship smartphone", "price": 749.99},
    {"name": "Google Pixel 6", "category": "Smartphone", "brand": "Google", "description": "Google's latest phone", "price": 599.99},
    {"name": "Samsung Galaxy A52", "category": "Smartphone", "brand": "Samsung", "description": "Mid-range smartphone", "price": 400.00},
    {"name": "OnePlus 9", "category": "Smartphone", "brand": "OnePlus", "description": "Premium flagship phone", "price": 699.99},
    {"name": "MacBook Pro 14-inch", "category": "Laptop", "brand": "Apple", "description": "Apple laptop with M1 Pro", "price": 1999.99},
    {"name": "MacBook Air", "category": "Laptop", "brand": "Apple", "description": "Ultra-portable laptop with M1", "price": 999.99},
    {"name": "Dell XPS 13", "category": "Laptop", "brand": "Dell", "description": "High-end Windows laptop", "price": 1499.99},
    {"name": "Lenovo ThinkPad X1 Carbon", "category": "Laptop", "brand": "Lenovo", "description": "Business ultrabook", "price": 1799.99},
    {"name": "Acer Predator Helios 300", "category": "Laptop", "brand": "Acer", "description": "Gaming laptop", "price": 1299.99},
    {"name": "HP Spectre x360", "category": "Laptop", "brand": "HP", "description": "Convertible laptop", "price": 1599.99},
    {"name": "Sony WH-1000XM4", "category": "Headphones", "brand": "Sony", "description": "Noise-cancelling headphones", "price": 348.00},
    {"name": "Bose QuietComfort 35 II", "category": "Headphones", "brand": "Bose", "description": "Noise-cancelling wireless headphones", "price": 299.99},
    {"name": "Apple AirPods Pro", "category": "Headphones", "brand": "Apple", "description": "Wireless noise-cancelling earbuds", "price": 249.99},
    {"name": "JBL Charge 4", "category": "Speaker", "brand": "JBL", "description": "Portable bluetooth speaker", "price": 149.99},
    {"name": "Sonos One", "category": "Speaker", "brand": "Sonos", "description": "Smart speaker with Alexa", "price": 199.99},
    {"name": "Amazon Echo Dot", "category": "Speaker", "brand": "Amazon", "description": "Smart speaker with Alexa", "price": 49.99},
    {"name": "Bang & Olufsen Beoplay A9", "category": "Speaker", "brand": "Bang & Olufsen", "description": "Premium home speaker", "price": 2499.99},
    {"name": "Nintendo Switch", "category": "Console", "brand": "Nintendo", "description": "Hybrid gaming console", "price": 299.99},
    {"name": "PlayStation 5", "category": "Console", "brand": "Sony", "description": "Next-gen gaming console", "price": 499.99},
    {"name": "Xbox Series X", "category": "Console", "brand": "Microsoft", "description": "Next-gen gaming console", "price": 499.99},
    {"name": "Oculus Quest 2", "category": "VR Headset", "brand": "Oculus", "description": "Wireless VR headset", "price": 299.99},
    {"name": "Fitbit Charge 5", "category": "Fitness Tracker", "brand": "Fitbit", "description": "Fitness tracking smartwatch", "price": 179.99},
    {"name": "Garmin Forerunner 945", "category": "Fitness Tracker", "brand": "Garmin", "description": "Advanced fitness smartwatch", "price": 599.99},
    {"name": "Apple Watch Series 7", "category": "Smartwatch", "brand": "Apple", "description": "Smartwatch with larger display", "price": 399.99},
    {"name": "Samsung Galaxy Watch 4", "category": "Smartwatch", "brand": "Samsung", "description": "Smartwatch with fitness tracking", "price": 249.99},
    {"name": "Sony A7 III", "category": "Camera", "brand": "Sony", "description": "Full-frame mirrorless camera", "price": 1999.99},
    {"name": "Canon EOS R5", "category": "Camera", "brand": "Canon", "description": "Mirrorless camera with 8K video", "price": 3899.99},
    {"name": "Nikon D850", "category": "Camera", "brand": "Nikon", "description": "High-resolution DSLR camera", "price": 2999.99},
    {"name": "GoPro Hero 10", "category": "Camera", "brand": "GoPro", "description": "Action camera with 5.3K video", "price": 499.99},
    {"name": "DJI Mavic Air 2", "category": "Drone", "brand": "DJI", "description": "4K drone with 34-minute battery", "price": 799.99},
    {"name": "Parrot Anafi", "category": "Drone", "brand": "Parrot", "description": "Compact drone with 4K camera", "price": 699.99},
    {"name": "Mac Mini with M1", "category": "Desktop", "brand": "Apple", "description": "Mini desktop with Apple's M1 chip", "price": 699.99},
    {"name": "Dell Inspiron Desktop", "category": "Desktop", "brand": "Dell", "description": "Affordable desktop for home or office", "price": 499.99},
    {"name": "HP Envy Desktop", "category": "Desktop", "brand": "HP", "description": "High-performance desktop", "price": 899.99},
    {"name": "Razer Blade 15", "category": "Laptop", "brand": "Razer", "description": "Gaming laptop", "price": 1599.99},
    {"name": "Microsoft Surface Laptop 4", "category": "Laptop", "brand": "Microsoft", "description": "Laptop with touchscreen", "price": 1299.99},
    {"name": "Alienware M15", "category": "Laptop", "brand": "Alienware", "description": "Gaming laptop", "price": 1799.99},
    {"name": "Xiaomi Mi 11", "category": "Smartphone", "brand": "Xiaomi", "description": "Flagship smartphone", "price": 749.99},
    {"name": "Motorola Edge 20", "category": "Smartphone", "brand": "Motorola", "description": "Mid-range smartphone", "price": 499.99},
    {"name": "Huawei P40 Pro", "category": "Smartphone", "brand": "Huawei", "description": "High-end smartphone", "price": 899.99},
    {"name": "Asus ROG Phone 5", "category": "Smartphone", "brand": "Asus", "description": "Gaming phone", "price": 999.99},
    {"name": "LG Velvet", "category": "Smartphone", "brand": "LG", "description": "Mid-range smartphone", "price": 450.00},
]

def populate_database():
    # Ensure the table is created before interacting with it
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        # Delete all existing data in the "items" table (safe because the table is now created)
        session.query(Item).delete()
        session.commit()

        # Add the new items to the database
        for item in initial_data:
            db_item = Item(
                name=item["name"],
                description=item["description"],
                price=item["price"],
                category=item["category"],
                brand=item["brand"]
            )
            session.add(db_item)

        session.commit()  # Commit the new items
        print("Database populated successfully with 50+ items!")

if __name__ == "__main__":
    populate_database()