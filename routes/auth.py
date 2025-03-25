from fastapi import APIRouter, HTTPException
from models import User
from database import db
from passlib.context import CryptContext  # For password hashing
import shortuuid

router = APIRouter(prefix="/auth", tags=["Auth"])

# Creating a password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    #Hashing the password before saving it.
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    #checking the password entered
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/signup")
async def signup(user: User):
    #Register new user
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_dict = user.model_dump()

    # Assigning a short 6-character string ID instead of ObjectID
    user_dict["_id"] = shortuuid.uuid()[:6]
    
    # hashing the password
    user_dict["password"] = hash_password(user_dict["password"])

    await db.users.insert_one(user_dict)
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: User):
    #Check the email existence in the db
    existing_user = await db.users.find_one({"email": user.email})
    
    #Validating the password
    if not existing_user or not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful"}
