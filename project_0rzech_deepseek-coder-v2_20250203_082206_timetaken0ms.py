 Sure! Below is a simple Python application that allows users to input their expenses and view them. This application uses a basic text-based interface for simplicity.

```python
class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, description, amount):
        expense = Expense(date, description, amount)
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for expense in self.expenses:
                print(f"Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (dd/mm/yyyy): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            tracker.add_expense(date, description, amount)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### How to Use the Application:
1. Run the script.
2. You will be presented with a menu with options to add an expense, view expenses, or exit the application.
3. Choose an option by entering the corresponding number.
4. For adding an expense, enter the date, description, and amount.
5. For viewing expenses, the application will list all the expenses you have added so far.
6. To exit the application, choose the "Exit" option.

This is a basic implementation and can be extended with more features like editing or deleting expenses, saving to a file, or using a graphical user interface.