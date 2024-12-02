from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app import models, schemas, database, security
from app.security import create_access_token
from app.models import User

router = APIRouter()

# Register a new user
@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Check if the username already exists
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hash the password
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password)
    
    # Add the user to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Return only the necessary fields for the response
    return schemas.User(id=db_user.id, username=db_user.username)


# Login route to get a token
@router.post("/login", response_model=schemas.Token)
def login_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    
    # Check if the user exists and the password matches
    if not db_user or not security.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Generate an access token
    access_token = security.create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# Protected route that requires authentication (Example: get user profile)
@router.get("/profile", response_model=schemas.User)
def get_user_profile(current_user: models.User = Depends(security.get_current_user)):
    return current_user
