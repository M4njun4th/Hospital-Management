from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables
MONGO_URL = os.getenv("MONGO_URL")

DATABASE_NAME = "Hospital_DB"

try:
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DATABASE_NAME]
    print(" MongoDB Connected Successfully!")
except Exception as e:
    print(" MongoDB Connection Failed:", e)


__all__ = ["db"]