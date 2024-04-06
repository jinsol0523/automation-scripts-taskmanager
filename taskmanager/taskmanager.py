import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def create_task():
    tasks = load_tasks()
    task_name = input("Enter task name: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    task = {"name": task_name, "due_date": due_date.strftime("%Y-%m-%d")}
    tasks.append(task)
    save_tasks(tasks)
    print("Task created successfully.")

def view_tasks():
    tasks = load_tasks()
    if tasks:
        task_list = "\n".join([f"{task['name']} - Due: {task['due_date']}" for task in tasks])
        print("Tasks:\n", task_list)
    else:
        print("No tasks found.")

def edit_task():
    tasks = load_tasks()
    if tasks:
        task_names = [task['name'] for task in tasks]
        selected_task = input("Select task to edit:\n" + "\n".join(task_names) + "\n")
        if selected_task in task_names:
            task_index = task_names.index(selected_task)
            new_name = input("Enter new task name (leave blank to keep the same): ")
            new_due_date_str = input("Enter new due date (YYYY-MM-DD) (leave blank to keep the same): ")
            if new_name:
                tasks[task_index]["name"] = new_name
            if new_due_date_str:
                try:
                    new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d")
                    tasks[task_index]["due_date"] = new_due_date.strftime("%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Task due date not changed.")
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Task not found.")
    else:
        print("No tasks found.")

def remove_task():
    tasks = load_tasks()
    if tasks:
        task_names = [task['name'] for task in tasks]
        selected_task = input("Select task to remove:\n" + "\n".join(task_names) + "\n")
        if selected_task in task_names:
            task_index = task_names.index(selected_task)
            del tasks[task_index]
            save_tasks(tasks)
            print("Task removed successfully.")
        else:
            print("Task not found.")
    else:
        print("No tasks found.")

def main():
    while True:
        print("\nTask Management System")
        print("1. Create Task\n2. View Tasks\n3. Edit Task\n4. Remove Task\n5. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
