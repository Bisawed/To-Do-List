# Creating a to do list with the following features:
# Add a task: Add a new task to the to-do list.
# View tasks: Display all the tasks in the to-do list.
# Complete a task: Mark a task as completed.
# Delete a task: Remove a task from the to-do list.

tasks = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")



def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i + 1}. {task['task']} - {status}")

def complete_task():
    view_tasks()
    task_num = int(input("Enter the task number to mark as complete: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as complete!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_num = int(input("Enter the task number to delete: "))
    if 0 < task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        print(f"Task '{deleted_task['task']}' deleted!")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
