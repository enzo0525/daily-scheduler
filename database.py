import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient(os.getenv('DATABASE_URL'))
db = client['daily_scheduler'] #Creates a new database
routines_collection = db['workouts']  #Creates a new database table inside the actual database

# routine = {
#     "user_id": 1,
#     "description": "Chest day",
#     "exercises": "x-y-z",
#     "date": "today"
# }

# routines_collection.insert_one(routine)
print("Routine inserted.")