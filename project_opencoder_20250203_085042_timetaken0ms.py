Sure, here is a simple Python application which captures expense details and calculates total expenses:

```python
class Expense:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def get_total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def display_expenses(self):
        print("Expenses:")
        for expense in self.expenses:
            print(f"Description: {expense['description']} Amount: {expense['amount']}")


def main():
    app = Expense()
    while True:
        action = input("\nEnter 'a' to add expense, 'v' to view expenses or 'q' to quit: ")

        if action.lower() == 'a':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            app.add_expense(description, amount)
        elif action.lower() == 'v':
            app.display_expenses()
            print(f"Total expenses: {app.get_total_expenses()}")
        elif action.lower() == 'q':
            break
        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
```

This is a simple command-line application that allows the user to add expense details and calculate total expenses. The user can view all added expenses, and quit the application when they're done.
