 1: Here is a simple example of how you can create a command line Todo application in Python. This program will allow users to add, list and remove tasks from their To-Do List.

```python
class TodoApp():
    def __init__(self):
        self.tasks = [] 
  
    def add_task(self, task): 
        if task not in self.tasks: # Avoid duplicate entries   
            self.tasks.append(task) 
            print('Task added successfully') 
        else: 
            print('This Task is already on your list!')  
          
    def remove_task(self, task): 
        if task in self.tasks: # Check if the task exists   
            self.tasks.remove(task) 
            print('Task removed successfully') 
        else: 
            print('This Task is not on your list!')  
          
    def list_all_tasks(self): 
        for i in self.tasks: print (i)   # Print all tasks if any exist else it will print empty     
                             
todo = TodoApp() # Create an instance of the class todo is object here  
while True:    # Infinite loop for continuous operation until user wants to quit 
    print("\n1.Add Task \n2.Remove Task \n3.List all tasks \n4.Quit")   
    choice = int(input('Enter your choice : '))  
      
    if choice == 1: # Add task option  
        task_name= input ('Enter the name of the task you want to add :') 
        todo.add_task(task_name)   # Call method from class instance     
                         
    elif choice==2: # Remove Task Option      
        if len(todo.tasks)>0:  # Check if any tasks exist before removing a task       
            task_name= input ('Enter the name of the task you want to remove :') 
            todo.remove_task(task_name)   # Call method from class instance     
        else: print('No Tasks available! Please add a Task first.')  
                         
    elif choice==3: # List all tasks option      
        if len(todo.tasks)>0:  # Check if any tasks exist before listing them       
            print ("Your Current To-Do list is : ") 
            todo.list_all_tasks()   # Call method from class instance     
        else: print('No Tasks available! Please add a Task first.')    
                         
    elif choice==4: # Quit option      
        break  # Break the infinite loop and end program 
```