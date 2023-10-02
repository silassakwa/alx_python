import requests
import sys

def get_employee_data(employee_id):
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

        # Calculate the number of completed tasks
        completed_tasks = [task for task in todo_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(todo_data)

        # Display the employee TODO list progress
        print(f"Employee {employee_data['name']} is done with tasks({num_completed_tasks}/{total_num_tasks}):")
        
        # Display the titles of completed tasks
        for task in completed_tasks:
            print(f"\t {task['title']}")

    else:
        print(f"Failed to retrieve data for employee ID {employee_id}")

if __name__ == "__main__":
    # Check if an employee ID was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)