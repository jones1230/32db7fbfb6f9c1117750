#!/usr/bin/python3
"""Returns information about his/her to-do list progress."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user data
    user = requests.get(url + 'users/{}'.format(employee_id)).json()
    # Fetch todo list data for the user
    todos = requests.get(url + 'todos',
                         params={"userId": employee_id}).json()

    # List of completed tasks
    completed = [todo for todo in todos if todo.get("completed")]

    # Output the required information
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get("name"), len(completed), len(todos)))

    # Output each completed task
    for task in completed:
        print('\t {}'.format(task.get("title")))
