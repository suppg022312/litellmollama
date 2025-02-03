 Creating a complex expenses app involves several components, including user authentication, database management, expense tracking, and reporting. Below, I'll outline a basic structure using Python with the Flask framework for the backend, and SQLite for the database. For the frontend, I'll suggest using React with TypeScript for a modern and robust user interface.

### Backend (Python with Flask)

1. **Setup Flask Environment**
2. **Database Setup with SQLite**
3. **User Authentication**
4. **Expense Tracking**
5. **Reporting**

### Frontend (React with TypeScript)

1. **Setup React Environment**
2. **User Interface**
3. **API Integration**

### Step 1: Setup Flask Environment

First, set up a new Flask project:

```bash
mkdir expenses_app
cd expenses_app
mkdir backend
cd backend
pipenv install Flask Flask-SQLAlchemy Flask-Migrate Flask-JWT-Extended
```

Create a `app.py` file:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
```

### Step 2: Database Setup with SQLite

Create a `models.py` file:

```python
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('expenses', lazy=True))
```

### Step 3: User Authentication

Create a `auth.py` file:

```python
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered"), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid username or password"), 401
```

### Step 4: Expense Tracking

Create a `routes.py` file:

```python
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, db
from models import Expense

@app.route('/expenses', methods=['POST'])
@jwt_required
def add_expense():
    amount = request.json.get('amount', None)
    description = request.json.get('description', None)
    user_id = get_jwt_identity()
    new_expense = Expense(amount=amount, description=description, user_id=user_id)
    db.session.add(new_expense)
    db.session.commit()
    return jsonify(message="Expense added"), 201

@app.route('/expenses', methods=['GET'])
@jwt_required
def get_expenses():
    user_id = get_jwt_identity()
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': e.id, 'amount': e.amount, 'description': e.description} for e in expenses]), 200
```

### Step 5: Reporting

Create a `reports.py` file for generating reports:

```python
from app import app, db
from models import Expense
from datetime import datetime, timedelta

@app.route('/reports/monthly', methods=['GET'])
def monthly_report():
    user_id = get_jwt_identity()
    today = datetime.today()
    start_date = datetime(today.year, today.month, 1)
    end_date = start_date + timedelta(days=31)
    expenses = Expense.query.filter(Expense.user_id == user_id, Expense.date >= start_date, Expense.date < end_date).all()
    total = sum([e.amount for e in expenses])
    return jsonify({'total': total}), 200
```

### Frontend (React with TypeScript)

1. **Setup React Environment**

```bash
npx create-react-app frontend --template typescript
cd frontend
npm install @mui/material @emotion/react @emotion/styled axios
```

2. **User Interface**

Create a simple UI for adding and viewing expenses.

3. **API Integration**

Use `axios` to make API requests.

```typescript
import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const registerUser = async (username, password) => {
    const response = await axios.post(`${API_URL}/register`, { username, password });
    return response.data;
};

export const loginUser = async (username, password) => {
    const response = await axios.post(`${API_URL}/login`, { username, password });
    if (response.data.access_token) {
        localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
};

export const addExpense = async (amount, description) => {
    const token = JSON.parse(localStorage.getItem('user')).access_token;
    const response = await axios.post(`${API_URL}/expenses`, { amount, description }, {
        headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
};

export const getExpenses = async () => {
    const token = JSON.parse(localStorage.getItem('user')).access_token;
    const response = await axios.get(`${API_URL}/expenses`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
};
```

### Summary

This setup provides a basic complex expenses app with user authentication, expense tracking, and reporting. You can extend this by adding more features like category management, budget tracking, and more sophisticated reporting.