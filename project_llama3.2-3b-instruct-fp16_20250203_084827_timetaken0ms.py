import datetime

class Expense:
    def __init__(self, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount
        self.date = datetime.datetime.now()

class ExpensesFormApp:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        category = input("Enter expense category: ")
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        expense = Expense(category, description, amount)
        self.expenses.append(expense)
        print(f"Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return
        for i, expense in enumerate(self.expenses):
            print(f"Expense {i+1}:")
            print(f"Category: {expense.category}")
            print(f"Description: {expense.description}")
            print(f"Amount: ${expense.amount:.2f}")
            print(f"Date: {expense.date.strftime('%Y-%m-%d')}\n")

    def calculate_total(self):
        if not self.expenses:
            return 0
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: ${total:.2f}")

def main():
    app = ExpensesFormApp()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            app.add_expense()
        elif choice == "2":
            app.view_expenses()
        elif choice == "3":
            app.calculate_total()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()