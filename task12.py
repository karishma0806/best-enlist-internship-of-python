import json 
from pymongo import MongoClient 


# Making Connection 
myclient = MongoClient("mongodb://localhost:27017/") 
 
db = myclient["GFG"] 

Collection = db["data"] 

with open('json.py') as file: 
	file_data = json.load(file) 
	
if isinstance(file_data, list): 
	Collection.insert_many(file_data) 
else: 
	Collection.insert_one(file_data) 
