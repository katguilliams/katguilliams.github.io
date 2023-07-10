import pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        #Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        self.client = MongoClient('localhost:27017'.format(username, password))
        #where xxxx is your unique port number
        self.database = self.client['AAC']
    
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            data_create = self.database.animals.insert(data)  # data should be dictionary
            return data_create
        else:
            raise Exception("Nothing to save, because data parameter is empty/incorrectly formatted")
            
# Create method to implement the R in CRUD.
    def read(self,data):
        if data is not None:    
            data_read = self.database.animals.find_one(data)
            return data_read
        else:
            raise Exception("Nothing to read because data parameter is empty/incorrectly formatted")
            
    def readAll(self, data):    
        data_read = self.database.animals.find(data,{"_id":False})   
        return data_read

# Create method to implement the U in CRUD.
    
    def update(self, query, data):
        if data is not None:    
            data_update = self.database.animals.update_one(query, data)
            return data_update
        else:
            raise Exception("Nothing to update because data parameter is empty/incorrectly formatted")
          
 # Create method to implement the D in CRUD.
    
    def delete(self,data):
        if data is not None:    
            data_delete = self.database.animals.delete_one(data)
            return data_delete
        else:
            raise Exception("Nothing to delete because data parameter is empty/incorrectly formatted")