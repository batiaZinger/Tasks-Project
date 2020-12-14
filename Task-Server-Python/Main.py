from flask_cors import CORS
import json
from flask import request, jsonify, send_file, Flask
from app import app
from datetime import datetime
import Sql_Function
from Common import Task, Task_List

CORS(app)


# get all the tasks from the data base
@app.route("/task", methods=['GET'])
def Get_All_Tasks():
    # call to a sql function to get all the tasks
    lst = list(Sql_Function.Get_All_Tasks())
    return jsonify({'result': [list(row) for row in lst]})


# get tasks by taskID from the data base
@app.route("/task/", methods=['GET'])
def Get_Task():
    # call to a sql function to get the task
    taskId = request.args['taskId']
    lst = list(Sql_Function.Get_Task(taskId))
    return jsonify({'result': [list(row) for row in lst]})


@app.route('/task', methods=['POST'])
def Create_Task():
    # get the new task
    data = request.get_json()
    # create a new task, and add - insert to the data base
    if data['taskEndDate'] is None:
        data['taskEndDate'] = ""
    Task_List.Create(data['taskName'], data['taskDescription'], data['taskStatus'], data['taskStartDate'],
                     data['taskEndDate'])
    return jsonify({'message': 'New task successfully added'})


@app.route('/task', methods=['PUT'])
def Update_Task():
    # get a task
    data = request.get_json()
    # update the task, and update in the data base
    Task_List.Update(data['taskID'], data['taskName'], data['taskDescription'], data['taskStatus'],
                     data['taskStartDate'],
                     data['taskEndDate'])
    return jsonify({'message': ' task is successfully updated'})


@app.route('/task/', methods=['DELETE'])
def Delete_Task():
    taskId = request.args['taskId']
    # delete the task
    Task_List.Delete(int(taskId))
    return jsonify({'message': ' task is successfully deleted'})


if __name__ == "__main__":
    app.run()
