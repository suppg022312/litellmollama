 Sure! Below is a simple implementation of a Todo app using Python and the `tkinter` library for the GUI. This app will allow you to add, remove, and view tasks.

```python
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")
        
        self.tasks = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=15)
        self.tasks_listbox.pack(pady=10)
        
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.RIGHT, padx=10)
        
        self.view_button = tk.Button(self.root, text="View Tasks", command=self.view_tasks)
        self.view_button.pack(side=tk.RIGHT, padx=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.tasks_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")
    
    def view_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
```

### How to Use:
1. **Add Task:** Enter the task in the text box and click "Add Task".
2. **Remove Task:** Select the task from the listbox and click "Remove Task".
3. **View Tasks:** Click "View Tasks" to see all the tasks in the listbox.

### Features:
- **Add Task:** Allows you to add a new task to the list.
- **Remove Task:** Allows you to remove a selected task from the list.
- **View Tasks:** Displays all the tasks currently in the list.

Feel free to customize this app further by adding more features or improving the UI.