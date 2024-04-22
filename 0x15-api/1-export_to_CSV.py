#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import sys
import requests
import csv


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_api = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url_api + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url_api + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
