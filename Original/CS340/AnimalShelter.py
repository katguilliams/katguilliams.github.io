import pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        #Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:45344' % (username, password))
        #where xxxx is your unique port number
        self.database = self.client['AAC']
    
#Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data) #data should be dictionary
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
#Create method to implement the R in CRUD.
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
        
        else:
            data = self.database.animals.find({}, {"_id": False})
        return data

#Create method to implement U in CRUD.
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {"$set": updateData})
        else:
            return "{}"
        return result.raw_result

#Create method to implement D in CRUD.
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        
        else:
            return "{}"
        return result.raw_result