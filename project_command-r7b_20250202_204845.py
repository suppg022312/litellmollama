Certainly! Below is a Python script that creates a simple expense tracking application using Streamlit, a popular library for building data apps. This script includes basic functionality to add, view, and manage expenses.

First, make sure you have Streamlit installed. You can install it using pip if you haven't already:

```sh
pip install streamlit
```

Now, create a file named `expenses_app.py` and paste the following code into it:

```python
import streamlit as st
from datetime import datetime

# Function to add an expense
def add_expense(date, category, amount):
    # For simplicity, we'll store expenses in a list. In a real application, you might want to use a database.
    if not st.session_state.get('expenses', []):
        st.session_state['expenses'] = []

    date = datetime.strptime(date, "%Y-%m-%d")  # Convert string to datetime object
    expense = {
        'date': date,
        'category': category,
        'amount': float(amount)
    }

    st.session_state['expenses'].append(expense)
    st.experimental_rerun()

# Streamlit app
st.set_option('deprecation.showFileOwner', False)

st.title("Expense Tracker")

with st.sidebar:
    st.header("Navigation")
    current_page = st.selectbox(
        "Select a page",
        ["Add Expense", "View Expenses"]
    )

if current_page == "Add Expense":
    st.subheader("Add Expense")

    date = st.date_input("Date", key="date_input")
    category = st.selectbox("Category", ["Food", "Rent", "Transportation", "Entertainment"])
    amount = st.number_input("Amount ($)", min_value=0.01, step=0.01)

    if st.button("Add Expense"):
        add_expense(date.strftime("%Y-%m-%d"), category, amount)

elif current_page == "View Expenses":
    st.subheader("Expenses")

    if 'expenses' not in st.session_state:
        st.session_state['expenses'] = []

    expenses = sorted(st.session_state.get('expenses', []), key=lambda x: x['date'])

    for expense in expenses:
        st.write(f"Date: {expense['date']} - Category: {expense['category']} - Amount: ${expense['amount']:.2f}")

```

### Explanation:

1. **Imports**: We import necessary libraries, including `streamlit` for the web interface and `datetime` for date handling.
2. **add_expense Function**: This function handles the addition of expenses. It converts the input date string to a `datetime` object, stores the expense in the session state, and re-runs the app to update the display.
3. **Streamlit App**: The main part of the script sets up the Streamlit app.
   - **Sidebar Navigation**: Users can choose between adding an expense or viewing expenses.
   - **Add Expense Page**: This page allows users to input date, category, and amount for a new expense.
   - **View Expenses Page**: This page displays all added expenses in a sorted list.
4. **Session State**: We use `st.session_state` to store the list of expenses so that it persists across sessions.

### Running the App:

1. Save the script as `expenses_app.py`.
2. Open a terminal and navigate to the directory where you saved the script.
3. Run the app using the following command:

```sh
streamlit run expenses_app.py
```

4. Open the URL provided in the terminal output (usually `http://localhost:8501`) in your web browser to interact with the app.

This is a basic example, and you can expand it with more features like editing expenses, filtering, and saving data persistently using a database.