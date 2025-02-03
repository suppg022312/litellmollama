 Sure! Below is a simple example of a To-Do app using Streamlit. This app will allow you to add, view, and delete tasks.

First, make sure you have Streamlit installed. You can install it using pip:

```sh
pip install streamlit
```

Now, create a Python file (e.g., `todo_app.py`) and paste the following code:

```python
import streamlit as st
import pandas as pd

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Title of the app
st.title('To-Do App')

# Input field for adding a task
task = st.text_input("Enter a task:")

# Button to add a task
if st.button("Add Task"):
    if task:
        st.session_state['tasks'].append(task)
        st.success(f"Added task: {task}")
    else:
        st.error("Task cannot be empty")

# Display tasks
st.subheader("Tasks")
if st.session_state['tasks']:
    for idx, task in enumerate(st.session_state['tasks']):
        st.write(f"{idx + 1}. {task}")
else:
    st.info("No tasks added yet.")

# Button to delete all tasks
if st.button("Delete All Tasks"):
    st.session_state['tasks'] = []
    st.success("All tasks have been deleted.")
```

To run the app, open a terminal, navigate to the directory where your `todo_app.py` file is located, and run:

```sh
streamlit run todo_app.py
```

This will start a local web server and open the app in your default web browser. You can now add, view, and delete tasks through the web interface.

Feel free to customize the app further by adding more features or improving the UI/UX.