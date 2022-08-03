import time
#from pymongo import MongoClient
#from flask import jsonify
#mongodb_client = MongoClient(uri="mongodb://mongodb:27017/mydb")
#db = mongodb_client.db

def function(n):
    time.sleep(5)
    output =  'output is -> '+str(len(n))
    return output
