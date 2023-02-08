#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            todo_req = requests.get(
                "{}todos/?userId={}".format(url, user)).json()
            task_completed = len(todo_req)
            completed = []
            for tasks in todo_req:
                if tasks.get("completed") is True:
                    completed.append(tasks)
            count = len(completed)
        print("Employee {} is done with tasks({}/{}):"
              .format(name, count, task_completed))
        for complete in completed:
            print("\t {}".format(complete.get("title")))
