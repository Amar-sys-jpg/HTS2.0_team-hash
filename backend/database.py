from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_SRV")  # Update if necessary
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.notify  # Database name
user_collection = database.get_collection("users")