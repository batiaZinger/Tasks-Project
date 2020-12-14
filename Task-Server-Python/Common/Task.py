# task definition

from enum import Enum


class Status(Enum):
    To_do = 1
    In_progress = 2
    Done = 3


class Task:
    def __init__(self, task_id, name, description, status, start_date, end_date=""):
        self.TaskID = task_id
        self.Name = name
        self.Description = description
        self.Status = status
        self.StartDate = start_date
        self.EndDate = end_date

    # return the task details
    def Task_Details(self):
        task_dict={}
        #put all the task properties in a dictionary
        for property, value in vars(self).items():
            task_dict.update({property : value})
        return task_dict
        # return "task ID: " + str(self.TaskID) + ",\n task name: " + self.Name + ",\n task description: " + self.Description + ",\n task status: " + self.Status \
        #        + ",\n task start date: " + self.StartDate + ",\n task end date: " + self.EndDate + "\n"

    #put all the task properties in a list
    def Convert_Object_List(self):
        # string = (
        #         str(self.TaskID) + "," + self.Name + "," + self.Description + "," + self.Status + "," + self.StartDate + "," + self.EndDate)
        # li = list(string.split(","))
        # return li
        task_list=[]
        for property, value in vars(self).items():
            task_list.append(value)
        return task_list
        # print(str(list))

# t = Task(0,'batia', 'bvshbvbvh', 'Done', '11.12.2020')
# t.Convert()
# print(str(t.Task_Details()))