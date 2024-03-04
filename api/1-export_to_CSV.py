import requests
import sys
import csv

def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Fetch employee's TODO list data
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todos = response.json()

    # Calculate TODO list progress
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    # Print employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")
    #creating csv file for the employee
    file_name = f"{employee_id}.csv"
    with open (file_name,"w", newline='') as csv_file:
        fieldnames=["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        
        '''write the csv headers'''
        writer.writeheader()
        for task in todos:
            writer.writerow({
                'USER_ID': employee_id,
                "USERNAME":employee_data['username'],
                "TASK_COMPLETED_STATUS":task["completed"],
                "TASK_TITLE": task['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_info(employee_id)
