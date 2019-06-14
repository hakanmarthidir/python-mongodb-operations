from pymongo import MongoClient
from bson.objectid import ObjectId


class ThermalRepository(object):

    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        self.database = self.client['thermalpythontomongo']

    def insert(self, project):
        if project is not None:
            insertedId = self.database.projects.insert_one(
                project.get_as_json()).inserted_id
            print(insertedId)
        else:
            raise Exception("Insert Exception")

    def get(self): 
        return self.database.projects.find({})
        
    def getbyId(self, id):
        return self.database.projects.find_one({"_id": ObjectId(id)})

    def update(self, project):
        if project is not None:
            self.database.projects.update({"_id": ObjectId(project._id)}, project.get_as_json())
        else:
            raise Exception("Update Exception")

    def delete(self, id):
        if id is not None:
            self.database.projects.remove({"_id": ObjectId(id)})
        else:
            raise Exception("Delete Exception")
