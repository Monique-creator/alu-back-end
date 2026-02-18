#!/usr/bin/python3
"""Fetches and displays employee TODO list progress from REST API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos".format(url),
                         params={"userId": employee_id}).json()

    completed = [t for t in todos if t.get("completed")]
    
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    
    for task in completed:
        print("\t {}".format(task.get("title")))
