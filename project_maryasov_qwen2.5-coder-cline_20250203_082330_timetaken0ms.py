Sure! Below is a simple example of an expense form app in Python. This app will allow users to input their expenses, save them to a file, and view all the saved expenses.

```python
import json

class ExpenseFormApp:
    def __init__(self):
        self.expenses = []
        self.file_path = 'expenses.json'

    def load_expenses(self):
        try:
            with open(self.file_path, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        expense = {}
        expense['date'] = input("Enter the date (YYYY-MM-DD): ")
        expense['description'] = input("Enter the description: ")
        expense['amount'] = float(input("Enter the amount: "))
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            for i, expense in enumerate(self.expenses, 1):
                print(f"{i}. Date: {expense['date']}, Description: {expense['description']}, Amount: ${expense['amount']}")

    def run(self):
        self.load_expenses()
        while True:
            print("\nExpense Form App")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.add_expense()
                self.save_expenses()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                print("Exiting the app...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ExpenseFormApp()
    app.run()
```

### How It Works:

1. **Loading and Saving Expenses**: The app loads expenses from a JSON file (`expenses.json`) when it starts and saves them back to the same file whenever an expense is added.

2. **Adding an Expense**: Users can enter details for a new expense, including the date, description, and amount. These details are stored in a dictionary and appended to the list of expenses.

3. **Viewing Expenses**: The app displays all the saved expenses in a simple format. Each expense is displayed with its index, date, description, and amount.

4. **Exiting the App**: Users can exit the app by selecting option 3.

### How to Run:

1. Save the code to a file named `expense_form_app.py`.
2. Run the script using Python:
   ```sh
   python expense_form_app.py
   ```

This is a basic example, and you can expand it with more features such as filtering expenses by date range, editing existing expenses, or deleting them.