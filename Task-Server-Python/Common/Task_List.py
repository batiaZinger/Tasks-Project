# create - add, update, delete tasks from the task list
from datetime import datetime

from Common import Task
import Sql_Function

# task list definition
# taskList = []
taskList = Sql_Function.Get_All_Tasks()


# create a task and add to the list
# function that get all the task details (name, description, status, start date, end date)
def Create(name, description, status, start_date, end_date=""):
    task_id = len(taskList)+1  # Automatic numbering
    task = Task.Task(task_id, name, description, status, start_date, end_date)
    taskList.append(task)
    Sql_Function.Task_Insert(task.Convert_Object_List())


# update a task in the task list
# the function get the task id And the updated details
def Update(task_id, name, description, status, start_date, end_date=""):
    task = Task.Task(task_id, name, description, status, start_date, end_date)
    # taskList[task_id] = task
    Sql_Function.Task_Update(task.Convert_Object_List())


# delete a task from the task list
# the function get the task id delete this task from the list
def Delete(task_id):
    # taskList.pop(task_id)
    Sql_Function.Task_Delete(task_id)


#
# Create('batia', 'bvshbvbvh', 'Done', datetime(2020, 12, 1))
# Create('deby', 'evjsri', 'To_do', datetime(2020, 8, 8), datetime(2020, 3, 9))
# Create('rina', 'ecnjsa', 'In_progress', datetime(2020, 11, 11), datetime(2020, 9, 11))
# for obj in taskList:
#     print(obj.Task_Details())
#Update(0, 'batia zinger', 'bvshbvbvh', 'In_progress', datetime(2020, 3, 12))
# Delete(2)
# for obj in taskList:
#     print(obj.Task_Details())
