import csv
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

        # Ensure User ID and Username are 25 characters long
        user_id = f"{employee_id:025}"
        username = f"{employee_data['username'][:25]:<25}"

        # Calculate the number of completed tasks
        completed_tasks = [task for task in todo_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(todo_data)

        # Display the employee TODO list progress
        print(f"User ID and Username: {user_id} - {username}")
        print(f"Employee {employee_data['name']} is done with tasks({num_completed_tasks}/{total_num_tasks}):")

        # Create and write the data to a CSV file
        csv_file_name = f"{user_id}.csv"
        with open(csv_file_name, mode='w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write the CSV header
            writer.writeheader()

            # Write each task as a row in the CSV file
            for task in todo_data:
                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": username,
                    "TASK_COMPLETED_STATUS": task["completed"],
                    "TASK_TITLE": task["title"]
                })

        print(f"Data exported to {csv_file_name}")

    else:
        print(f"Failed to retrieve data for employee ID {employee_id}")

if __name__ == "__main__":
    # Check if an employee ID was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)