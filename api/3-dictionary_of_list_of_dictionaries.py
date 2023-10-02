import json
import requests


def get_all_employee_data():
    # Define the URL for all employees
    all_users_url = "https://jsonplaceholder.typicode.com/users"

    # Make an API request to fetch all employees
    users_response = requests.get(all_users_url)

    # Check if the request was successful
    if users_response.status_code == 200:
        users_data = users_response.json()

        # Create a dictionary to store the JSON data for all employees and tasks
        json_data = {}

        for user in users_data:
            # Fetch individual employee's TODO list
            employee_id = user["id"]
            employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            todo_response = requests.get(employee_url)

            # Check if the TODO list request was successful
            if todo_response.status_code == 200:
                todo_data = todo_response.json()

                # Create a list to store tasks for the current employee
                tasks_list = []

                for task in todo_data:
                    tasks_list.append({
                        "username": user["username"],
                        "task": task["title"],
                        "completed": task["completed"]
                    })

                # Add tasks list to JSON data with the USER_ID as the key
                json_data[user["id"]] = tasks_list

        # Create a JSON file and write the data to it
        json_file_name = "todo_all_employees.json"
        with open(json_file_name, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {json_file_name}")

        # Output the data for all users found
        for user_id, tasks in json_data.items():
            print(f"User ID: {user_id}")
            for task in tasks:
                print(f"Username: {task['username']}")
                print(f"Task: {task['task']}")
                print(f"Completed: {task['completed']}")
                print()

    else:
        print("Failed to retrieve data for all employees")

if __name__ == "__main__":
    get_all_employee_data()