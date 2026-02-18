#!/usr/bin/python3
"""Module to fetch employee TODO list progress from REST API."""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(
        base_url, employee_id))
    employee_name = user_response.json().get("name")

    todos_response = requests.get("{}/todos?userId={}".format(
        base_url, employee_id))
    todos = todos_response.json()

    completed = [task for task in todos if task.get("completed") is True]
    total_tasks = len(todos)
    completed_tasks = len(completed)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))

    for task in completed:
        print("\t {}".format(task.get("title")))
