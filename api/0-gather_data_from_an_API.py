#!/usr/bin/python3
"""
Accesses a REST API for a given employee ID and returns
information about his/her list progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user data
    user_req = requests.get(url + "users/{}".format(user_id))
    user_name = user_req.json().get("name")

    # Fetch todo data
    todos_req = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_req.json()

    completed_tasks = [t.get("title") for t in todos if t.get("completed")]
    total_tasks = len(todos)
    done_count = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, done_count, total_tasks))
    
    for task in completed_tasks:
        print("\t {}".format(task))
