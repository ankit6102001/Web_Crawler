from pymongo import MongoClient

def get_mongo_client(db_url='mongodb://localhost:27017/', db_name='web_crawler'):
    client = MongoClient(db_url)
    return client[db_name]

def store_data_to_mongo(data, db_url='mongodb://localhost:27017/', db_name='web_crawler'):
    db = get_mongo_client(db_url, db_name)
    collection = db.scraped_data  
    collection.insert_one(data)
