from bson.objectid import ObjectId


class Parameter(object):

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class Project(object):

    def __init__(self, project_id=None, title=None, description=None, parameter=Parameter()):
        if project_id is None:
            self._id = ObjectId()
        else:
            self._id = project_id
        self.title = title
        self.description = description
        self.parameter = parameter
        

    def get_as_json(self):
        return self.__dict__

    @staticmethod
    def build_from_json(json_data):
        if json_data is not None:
            try:
                return Project(json_data.get('_id', None),
                               json_data['title'],
                               json_data['description'],
                               json_data['parameter']
                               )
            except KeyError as e:
                raise Exception(
                    "Key not found in json_data: {}".format(e.message))
        else:
            raise Exception("No data to create Project from!")
