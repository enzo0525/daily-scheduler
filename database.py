import pymongo
from dotenv import load_dotenv
import os
from bson import ObjectId

load_dotenv()

client = pymongo.MongoClient(os.getenv('DATABASE_URL'))
db = client['daily_scheduler'] #Creates a new database if doesn't exist already
tasks_collection = db['routine']  #Creates a new database table inside the actual database if doesn't exist already

def add_task_database(data):
    tasks_collection.insert_one(data)
    print("Routine inserted.")

def remove_task_database(id):
    data = ObjectId(id)
    if tasks_collection.delete_one(filter={
        '_id': data
    }):
        return True
    return False
    

def get_all_routines():
    return list(tasks_collection.find())