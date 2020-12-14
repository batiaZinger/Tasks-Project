import json

import pyodbc
from datetime import datetime

# connect to data base
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-2M1D23EP;'
                      'Database=TasksDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


# get all the tasks from the data base
def Get_All_Tasks():
    a = list(cursor.execute('SELECT * FROM Task'))
    return a

# get tasks by taskID from the data base
def Get_Task(task_id):
    sql_command = """
                    select * from TasksDB.dbo.Task 
                    where taskID = ?
                """
    a = list(cursor.execute(sql_command, task_id))
    return a


# insert a task into the tasks table
def Task_Insert(lst):
    sql_command = """INSERT INTO TasksDB.dbo.Task (taskID, taskName, taskDescription, taskStatus, taskStartDate, taskEndDate)
                     VALUES (?, ?, ?, ?, ?, ?);"""

    cursor.execute(sql_command, int(lst[0]), lst[1], lst[2], lst[3], lst[4], lst[5])
    conn.commit()


# update the task
def Task_Update(lst):
    sql_command = """
             update TasksDB.dbo.Task 
             set taskName = ?, taskDescription = ?, taskStatus = ?, taskStartDate = ?, taskEndDate = ?
             where taskID = ?
                """
    cursor.execute(sql_command, lst[1], lst[2], lst[3], lst[4], lst[5], int(lst[0]))
    conn.commit()


# delete task from the data base
def Task_Delete(task_id):
    sql_command = """
                delete from TasksDB.dbo.Task 
                where taskID = ?
                """
    cursor.execute(sql_command, task_id)
    conn.commit()

