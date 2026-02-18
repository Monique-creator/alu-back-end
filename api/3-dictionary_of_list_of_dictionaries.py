#!/usr/bin/python3
"""
Exports TODO list data of all employees to a single JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    
    users = requests.get(url + "users").json()
    all_tasks = {}

    for user in users:
        u_id = str(user.get("id"))
        u_name = user.get("username")
        todos = requests.get(url + "todos", params={"userId": u_id}).json()
        
        all_tasks[u_id] = [
            {
                "username": u_name,
                "task": t.get("title"),
                "completed": t.get("completed")
            } for t in todos
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
