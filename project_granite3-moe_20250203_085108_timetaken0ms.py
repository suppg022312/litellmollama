```python
class Expense:
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f"Expense(amount={self.amount}, date={self.date})"

class ExpensesForm:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def display_expenses(self):
        print("Expenses:")
        for expense in self.expenses:
            print(expense)

# Example usage:
form = ExpenseForm()
form.add_expense(Expense(100, "2022-01-01"))
form.add_expense(Expense(200, "2022-02-15"))
form.display_expenses()
```

This Python code creates an `Expense` class to represent individual expenses and an `ExpensesForm` class to manage a list of expenses. The example usage at the end of the code demonstrates how to use these classes to add, display, and manage expenses.