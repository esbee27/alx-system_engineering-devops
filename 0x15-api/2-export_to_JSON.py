#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))
    name = user.json().get('username')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    todoUsr = {}
    taskLst = []

    for task in todos.json():
            if task.get('userId') == int(userId):
                taskDict = {"task": task.get('title'), "completed": task.get('completed'), "username": user.json().get('username')}
                taskLst.append(taskDict)
    todoUsr[userId] = taskLst

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUsr, f)
