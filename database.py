import pymongo
import os
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

client = pymongo.MongoClient(os.getenv('DATABASE_URL'))
db = client['daily_scheduler'] #Creates a new database if doesn't exist already.
tasks_collection = db['routine']  #Creates a new database table inside the actual database if doesn't exist already.
discord_id_collection = db['discord_id']

def add_task_database(data): #Adds data to database, return true if good, else returns false if catches any errors.
    try:
        tasks_collection.insert_one(data)
        return True
    except Exception as e:
        print(f'ERROR when adding to the database: {e}')
        return False

def remove_task_database(id): #Removes data from database, if the count of deleted items is 1, return true, if any errors, returns false.
    try:
        data_id_to_delete = ObjectId(id)
        result = tasks_collection.delete_one({'_id': data_id_to_delete})
        if result.deleted_count == 1:
            return True
    except Exception as e:
        print(f'ERROR when deleting from database: {e}')
        return False

def get_all_routines(): #Returns all data from database.
    if is_database_empty():
        return False

    routines_list = list(tasks_collection.find())
    for routine in routines_list:
        routine['_id'] = str(routine['_id'])

    return routines_list

def get_routine_from_day(day):
    return list(tasks_collection.find({'taskDayOfWeek': str(day)}, {'_id': False}))

def is_database_empty():
    return tasks_collection.count_documents({}) == 0

def set_discord_id(data): #try adding to database, if theres a number there, delete it and replace it, if not just add, return true if ok, false if bad
    try:
        if discord_id_collection.count_documents({}) == 1:
            discord_id_collection.find_one_and_replace(filter={}, replacement=data)
            print('discord_id found and replaced')
            return True
        discord_id_collection.insert_one(data)
        print('discord_id inserted')
        return True 
    except Exception as e:
        print(f'ERROR when setting phone number in database: {e}')
        return False
    
def get_discord_id():
    return list(discord_id_collection.find({}, {'_id': False}))[0]['discord_id']