Sure! Here's a basic structure for an expenses form application in Python:

```python
class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
    
    def display(self):
        print(f"{self.description}: {self.amount}")
    

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    return Expense(description, amount)
    


def main():
    expenses = []
    
    while True:
        action = input("""\nActions:
1. Add an expense
2. View all expenses
3. Exit\n""")
        
        if action == '1':
            new_expense = add_expense()
            expenses.append(new_expense)
            
        elif action == '2':
            for exp in expenses:
                exp.display()
                
        elif action == '3':
            break
        
        else:
            print("Invalid option. Please try again.")
    
    print("\nExpenses form application closed.")

if __name__ == "__main__":
    main()
```
This script creates an Expenses Form Application, where you can add expenses and view all added expenses.