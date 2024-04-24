#!/usr/bin/python3
"""use json plasceholder to get employee todo list"""


from requests import get
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    todo_url = url + "/user/{}/todos".format(sys.argv[1])
    name_url = url + "/users/{}".format(sys.argv[1])
    todo_list = get(todo_url).json()
    name_result = get(name_url).json()

    todo_len = len(todo_list)
    todo_complete = len([todo for todo in todo_list
                         if todo.get("completed")])
    employee = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(employee, todo_complete, todo_len))
    for todo in todo_list:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
