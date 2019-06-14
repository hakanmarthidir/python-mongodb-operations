from project import Project
from thermalrepository import ThermalRepository


def get(repository):
    projects = repository.get()
    for p in projects:
        tmp_project = Project.build_from_json(p)
        print(tmp_project._id, tmp_project.title,
              tmp_project.description, tmp_project.parameter['x'])


def getbyId(repository, id):
    projects = repository.getbyId(id)
    project = Project.build_from_json(projects)
    return project


def create(repository, project):
    repository.insert(project)
    print("Project was created successfully")


def update(repository, project):
    repository.update(project)
    print("Project was updated")


def delete(repository, project):
    repository.delete(project)
    print("Project was deleted")


def main():
    repository = ThermalRepository()

    # Step 1 - Create a Project
    # project = Project.build_from_json({"title": "ThermalBridge2",
    # "description": "ThermalBridge2 Project Long Desc",
    # "parameter": {"x": 1, "y": 2, "z": 3}})
    #create(repository, project)

    # Step 2 - Get Datas
    #get(repository)
    
    #project = getbyId(repository,"5d0257d7683125e73e3de161")
    #print(project.description)

    # Step 3 - Update Data
    #updatedProject = getbyId(repository,'5d024f5816587cbbe7aa3de1')
    #updatedProject.description = "ThermalBridge Short Desc"
    #update(repository, updatedProject)
    #get(repository)

    # Step 4 - Delete Data
    #delete(repository, '5d024f5816587cbbe7aa3de1')
    #get(repository)

if __name__ == '__main__':
    main()
