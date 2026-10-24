# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'password' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if not isinstance(data, dict) or not data: #this validates the input format
            return False
        try:  #this inserts the document into MongoDB
            result = self.collection.insert_one(data)
            return result.acknowledged #MongoDB ack when the inport succeeds
        except Exception as error: #This outputs the error if one occurs
            print(f"Error importing document: {error}")
            return False

    # Create method to implement the R in CRUD.
    
    def read(self, query): #this validates that the query is a dictionary
        if not isinstance(query, dict):
            return[]
        
        try: # this returns a MongoDB cursor with matches
            cursor = self.collection.find(query)
            #this converts the cursor to a list
            return list(cursor)
        
        except Exception as error:
            #this outputs an error message if one occurs
            print(f"error reading documents: {error}")
            return[]
        
    # Create method to implement the U in CRUD
    
    def update(self, query, update_data):
        
        # This checks to see if the update contains at least 1 value and is a dictionary
        if not isinstance(query, dict) or not isinstance (update_data, dict) or not update_data:
            return 0
        
        try:
            #This updates all documents that match the query
            result = self.collection.update_many(
                query,
                {"$set": update_data}
            )
            #This returns the number of documents updated
            return result.modified_count
        
        except Exception as error:
            #This returns zero if the database update fails
            print(f"Error updating documents: {error}")
            return 0
        
    #Create method to implement the D in CRUD
        
    def delete(self, query):
        
        #This checks if the query is a dictionary
        if not isinstance(query, dict):
            return 0
        
        try: 
            
            #This deletes all documents that match the query
            result = self.collection.delete_many(query)
            
            #This returns the number of documents removed
            return result.deleted_count
        
        except Exception as error:
            
            #This returns zero if delete fails
            print(f"Error deleting documents: {error}")
            return 0