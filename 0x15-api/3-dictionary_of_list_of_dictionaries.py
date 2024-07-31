#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = user.json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()

    allTodos = {}

    { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
