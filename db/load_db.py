from pymongo import MongoClient
import json
from pathlib import Path

client = MongoClient()
print(client.list_database_names())
db = client["access"]
collection = db["2022"]
for year_dir in Path('/home/pinbo/Documents/Plagiarism-Check/data').glob('*'):
    print('*'*50)
    print('*'*50)
    print('*'*50)
    print("Working on: ", year_dir)
    if year_dir.is_dir():
        for doc in year_dir.glob('*'):
            print('-'*50)
            print("Inserting: ", year_dir, "into DB")
            print("Name:", doc.name)
            with open(doc, "r") as file:
                file_data = json.load(file)
                collection.insert_one(file_data)
client.close()
