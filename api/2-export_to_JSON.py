import json
import requests
import sys

def get_employee_data(employee_id):
    """
    Fetches employee data and their TODO list, then exports it to a JSON file.

    Args:
        employee_id (int): The ID of the employee for whom data is to be fetched and exported.

    Returns:
        None
    """
    # Define the API URLs for employee details and their TODO list
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Make API requests to fetch employee details and TODO list
    employee_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)

    # Check if both requests were successful
    if employee_response.status_code == 200 and todo_response.status_code == 200:
        employee_data = employee_response.json()
        todo_data = todo_response.json()

        # Create a dictionary to store the JSON data
        json_data = {
            "USER_ID": [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_data["username"]
                }
                for task in todo_data
            ]
        }

        # Create a JSON file and write the data to it
        json_file_name = f"{employee_id}.json"
        with open(json_file_name, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {json_file_name}")

    else:
        print(f"Failed to retrieve data for employee ID {employee_id}")

if __name__ == "__main__":
    # Check if an employee ID was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)