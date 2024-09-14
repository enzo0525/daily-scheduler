import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient(os.getenv('DATABASE_URL'))
db = client['daily_scheduler'] #Creates a new database if doesn't exist already
tasks_collection = db['routine']  #Creates a new database table inside the actual database if doesn't exist already

def add_task_database(data):
    tasks_collection.insert_one(data)
    print("Routine inserted.")

def remove_task_database(dataId): # To do
    pass