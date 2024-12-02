from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app import schemas, models, database
from sqlalchemy.orm import Session
from passlib.context import CryptContext  # Add this import for password hashing

# Define the OAuth2PasswordBearer instance
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Secret key for encoding the JWT token
SECRET_KEY = "a5ec847ae78b89a57654bfedbbf56cb2030f2151abdece91c92d6a19b5a6da46"

ALGORITHM = "HS256"  # You can adjust the algorithm as needed
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Set the expiration time of the access token in minutes

# Initialize CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash passwords
def get_password_hash(password: str) -> str:
    """
    Hash a password using bcrypt.
    """
    return pwd_context.hash(password)

# Function to verify passwords
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

# Function to create access tokens
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    """
    Generates a JWT token with the provided data and expiration time.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)) -> models.User:
    """
    Decodes the token and retrieves the user from the database.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = db.query(models.User).filter(models.User.username == username).first()  # Check the user by username
        if user is None:
            raise credentials_exception
    except JWTError as e:
        print(f"JWT decode error: {e}")  # Add error logging
        raise credentials_exception
    return user
