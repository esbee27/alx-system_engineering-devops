#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""

import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))
    name = user.json().get('username')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    filename = userId + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, str(task.get('completerd')), task.get('title')])
