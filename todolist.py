import json
import os

TODO_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet!")
    else:
        print("\n📋 To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{idx}. {task['task']} [{status}]")

# Main menu
def menu():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter task description: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)

        elif choice == '2':
            show_tasks(tasks)

        elif choice == '3':
            show_tasks(tasks)
            num = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]['done'] = True
                save_tasks(tasks)

        elif choice == '4':
            show_tasks(tasks)
            num = int(input("Enter task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
                save_tasks(tasks)

        elif choice == '5':
            print("Exiting... 👋")
            break

        else:
            print("Invalid choice. Try again.")

# Run the app
menu()
