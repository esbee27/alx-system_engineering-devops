#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()

    allTodos = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDic = {"username": user.get('name'), "task": task.get('title'), "completed": task.get('completed')}
                taskList.append(taskDic)
        allTodos[user.get('id')] = taskList
with open("todo_all_employees.json", mode='w') as f:
    json.dump(allTodos, f)
