#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import sys
import json
import requests

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_api = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url_api + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url_api + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
