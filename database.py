import pymongo
import os
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

client = pymongo.MongoClient(os.getenv('DATABASE_URL'))
db = client['daily_scheduler'] #Creates a new database if doesn't exist already.
tasks_collection = db['routine']  #Creates a new database table inside the actual database if doesn't exist already.

def add_task_database(data): #Adds data to database, return true if good, else returns false if catches any errors.
    try:
        tasks_collection.insert_one(data)
        return True
    except Exception as e:
        print('ERROR when adding to the database.')
        print(e)
        return False

def remove_task_database(id): #Removes data from database, if the count of deleted items is 1, return true, if any errors, returns false.
    try:
        data = ObjectId(id)
        result = tasks_collection.delete_one({'_id': data})
        if result.deleted_count == 1:
            return True
    except Exception as e:
        print('ERROR when deleting from database.')
        print(e)
        return False

def get_all_routines(): #Returns all data from database.
    if is_database_empty():
        return False

    routines_list = list(tasks_collection.find())
    for routine in routines_list:
        routine['_id'] = str(routine['_id'])

    return routines_list

def is_database_empty():
    return len(list(tasks_collection.find())) == 0


#make a function to check the length of database, if its 0, display that there are no routines, else display routines
#keep track of it, every time something is deleted, update the value and check if its length is 0 or > 0