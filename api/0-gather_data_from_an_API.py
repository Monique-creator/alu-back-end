#!/usr/bin/python3
"""
Script that fetches employee TODO list progress from REST API.
Displays completed tasks for a given employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee data
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Fetch TODO list
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)
    
    # Print employee progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    
    # Print completed task titles
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
