 Creating a complex expenses app using Python and Streamlit involves several steps. Below is a basic example to get you started. This example will include a simple login system, adding expenses, viewing expenses, and categorizing expenses.

First, make sure you have Streamlit and other dependencies installed. You can install them using pip:

```bash
pip install streamlit pandas
```

Now, let's create a simple expenses app.

1. **Create a new Streamlit app**: Create a new Python file, e.g., `expenses_app.py`.

2. **Set up the login system**: We'll use a basic username and password for simplicity.

3. **Add expenses and view expenses**: We'll use a DataFrame to store expenses.

4. **Categorize expenses**: We'll add categories to the expenses.

Here's the complete code:

```python
import streamlit as st
import pandas as pd
import os

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = pd.DataFrame(columns=['Date', 'Description', 'Amount', 'Category'])

# Login page
def login():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if username == 'admin' and password == 'password':
            st.session_state['logged_in'] = True
        else:
            st.error('Invalid username or password')

# Main page
def main():
    if not st.session_state['logged_in']:
        login()
    else:
        st.title('Expenses App')
        st.write('Welcome, ' + username + '!')
        add_expense()
        view_expenses()

# Add expense page
def add_expense():
    st.sidebar.title('Add Expense')
    with st.sidebar.form(key='expense_form'):
        date = st.date_input('Date')
        description = st.text_input('Description')
        amount = st.number_input('Amount', step=1.0)
        category = st.selectbox('Category', ['Food', 'Transport', 'Housing', 'Entertainment', 'Other'])
        submit_button = st.form_submit_button(label='Add Expense')
        if submit_button:
            new_expense = {'Date': date, 'Description': description, 'Amount': amount, 'Category': category}
            st.session_state['expenses'] = st.session_state['expenses'].append(new_expense, ignore_index=True)
            st.success('Expense added successfully!')

# View expenses page
def view_expenses():
    st.sidebar.title('View Expenses')
    expenses = st.session_state['expenses']
    category = st.sidebar.selectbox('Filter by Category', ['All'] + list(expenses['Category'].unique()))
    if category == 'All':
        filtered_expenses = expenses
    else:
        filtered_expenses = expenses[expenses['Category'] == category]
    st.write(filtered_expenses)
    total_amount = filtered_expenses['Amount'].sum()
    st.write(f'Total Amount: ${total_amount:.2f}')

# Run the app
if __name__ == '__main__':
    main()
```

### Explanation:

1. **Login System**:
    - The `login` function handles the login process. It checks if the username and password are correct.
    - If the login is successful, it sets `st.session_state['logged_in']` to `True`.

2. **Main Page**:
    - The `main` function checks if the user is logged in. If not, it shows the login page.
    - If the user is logged in, it shows the main app with options to add and view expenses.

3. **Add Expense**:
    - The `add_expense` function allows the user to add a new expense.
    - It uses a form to collect the date, description, amount, and category.
    - The new expense is appended to the DataFrame in `st.session_state['expenses']`.

4. **View Expenses**:
    - The `view_expenses` function allows the user to filter expenses by category.
    - It displays the filtered expenses and the total amount.

### Running the App:

To run the app, navigate to the directory containing your `expenses_app.py` file and run:

```bash
streamlit run expenses_app.py
```

This will start a local web server and open the app in your default web browser.

Feel free to expand this basic example with additional features such as editing and deleting expenses, exporting data to CSV, and more sophisticated user management.