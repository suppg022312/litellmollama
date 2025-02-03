 Sure! Below is a simple implementation of a Todo app using Python. This app will allow you to add, view, and remove tasks. For simplicity, we'll use a list to store the tasks and a loop to handle user input.

```python
def show_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### How to Use the Todo App:
1. **Add Task**: Enter `1` and then type the task you want to add.
2. **View Tasks**: Enter `2` to see all the tasks.
3. **Remove Task**: Enter `3` and then type the number of the task you want to remove.
4. **Exit**: Enter `4` to exit the app.

Feel free to modify and expand this app to suit your needs!