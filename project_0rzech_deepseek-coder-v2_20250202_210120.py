 Creating a complex Python project for an expenses claim app involves several steps, including planning, designing, coding, and testing. Below is a simplified version of such a project. This example will cover the basic functionalities such as user authentication, expense submission, approval, and reporting.

### Project Structure

```
expenses_claim_app/
├── app.py
├── models.py
├── views.py
├── controllers.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── submit_expense.html
│   ├── expenses_list.html
├── static/
│   ├── css/
│   ├── js/
├── migrations/
├── requirements.txt
```

### Step 1: Set Up the Project

1. **Create a virtual environment and install dependencies:**

```bash
mkdir expenses_claim_app
cd expenses_claim_app
python3 -m venv venv
source venv/bin/activate
pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF Flask-Migrate
```

2. **Initialize the project structure:**

```bash
mkdir templates static migrations
touch app.py models.py views.py controllers.py requirements.txt
```

### Step 2: Define the Models

**models.py:**

```python
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('expenses', lazy=True))
```

### Step 3: Create the Flask App

**app.py:**

```python
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Expense
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', expenses=expenses)

@app.route('/submit_expense', methods=['GET', 'POST'])
@login_required
def submit_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        expense = Expense(description=description, amount=amount, user_id=current_user.id)
        db.session.add(expense)
        db.session.commit()
        flash('Expense submitted successfully', 'success')
        return redirect(url_for('dashboard'))
    return render_template('submit_expense.html')

@app.route('/expenses_list')
@login_required
def expenses_list():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    expenses = Expense.query.all()
    return render_template('expenses_list.html', expenses=expenses)

@app.route('/approve_expense/<int:expense_id>', methods=['POST'])
@login_required
def approve_expense(expense_id):
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    expense = Expense.query.get_or_404(expense_id)
    expense.status = 'Approved'
    db.session.commit()
    flash('Expense approved', 'success')
    return redirect(url_for('expenses_list'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 4: Create the Templates

**templates/base.html:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Expenses Claim App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1>Expenses Claim App</h1>
        <nav>
            <ul>
                <li><a href="{{ url_for('dashboard') }}">Dashboard</a></li>
                <li><a href="{{ url_for('submit_expense') }}">Submit Expense</a></li>
                <li><a href="{{ url_for('expenses_list') }}">Expenses List</a></li>
                <li><a href="{{ url_for('logout') }}">Logout</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="flashes">
                    {% for category, message in messages %}
                        <div class="{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**templates/login.html:**

```html
{% extends "base.html" %}

{% block content %}
    <form method="POST">
        <h2>Login</h2>
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Login</button>
    </form>
{% endblock %}
```

**templates/dashboard.html:**

```html
{% extends "base.html" %}

{% block content %}
    <h2>Dashboard</h2>
    <a href="{{ url_for('submit_expense') }}">Submit New Expense</a>
    <table>
        <thead>
            <tr>
                <th>Description</th>
                <th>Amount</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for expense in expenses %}
                <tr>
                    <td>{{ expense.description }}</td>
                    <td>{{ expense.amount }}</td>
                    <td>{{ expense.status }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

**templates/submit_expense.html:**

```html
{% extends "base.html" %}

{% block content %}
    <form method="POST">
        <h2>Submit Expense</h2>
        <div>
            <label for="description">Description:</label>
            <input type="text" id="description" name="description" required>
        </div>
        <div>
            <label for="amount">Amount:</label>
            <input type="number" id="amount" name="amount" step="0.01" required>
        </div>
        <button type="submit">Submit</button>
    </form>
{% endblock %}
```

**templates/expenses_list.html:**

```html
{% extends "base.html" %}

{% block content %}
    <h2>Expenses List</h2>
    <table>
        <thead>
            <tr>
                <th>Description</th>
                <th>Amount</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for expense in expenses %}
                <tr>
                    <td>{{ expense.description }}</td>
                    <td>{{ expense.amount }}</td>
                    <td>{{ expense.status }}</td>
                    <td>
                        {% if not expense.is_admin %}
                            <form method="POST" action="{{ url_for('approve_expense', expense_id=expense.id) }}" style="display:inline;">
                                <button type="submit">Approve</button>
                            </form>
                        {% endif %}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

### Step 5: Run the Application

1. **Create a migration script:**

```bash
flask db init
flask db migrate
flask db upgrade
```

2. **Run the application:**

```bash
flask run
```

This is a basic implementation of an expenses claim app. You can further enhance this project by adding more features like user roles, better error handling, and a more robust UI.