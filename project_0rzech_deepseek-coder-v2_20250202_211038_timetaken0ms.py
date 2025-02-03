 Creating a complex Python project for an expenses claim app involves several components, including a backend API, a database, a web interface, and possibly a mobile app. For simplicity, I'll focus on the backend API and a basic web interface using Flask for the web server and SQLAlchemy for the database.

### Project Structure

1. **`app/`**: Main application directory.
2. **`app/models.py`**: Database models.
3. **`app/routes.py`**: Flask routes.
4. **`app/forms.py`**: Flask-WTF forms.
5. **`app/templates/`**: HTML templates.
6. **`app/static/`**: Static files (CSS, JS, images).
7. **`app/config.py`**: Configuration settings.
8. **`app/main.py`**: Entry point of the application.
9. **`tests/`**: Test cases.

### Dependencies

You'll need to install Flask and SQLAlchemy. You can use pip to install these:

```bash
pip install Flask SQLAlchemy Flask-WTF Flask-Login
```

### Code

#### `app/config.py`

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///expense_claims.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

#### `app/models.py`

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    claims = db.relationship('Claim', backref='author', lazy='dynamic')

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
```

#### `app/routes.py`

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from app.forms import ClaimForm
from app.models import db, User, Claim

app = Flask(__name__)
app.config.from_object('app.config.Config')
db.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    claims = Claim.query.order_by(Claim.date.desc()).all()
    return render_template('index.html', claims=claims)

@app.route('/claim', methods=['GET', 'POST'])
def claim():
    form = ClaimForm()
    if form.validate_on_submit():
        claim = Claim(description=form.description.data,
                      amount=form.amount.data,
                      author=current_user)
        db.session.add(claim)
        db.session.commit()
        flash('Your claim has been submitted!')
        return redirect(url_for('index'))
    return render_template('claim.html', title='Submit a Claim', form=form)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Claim': Claim}

if __name__ == '__main__':
    app.run(debug=True)
```

#### `app/forms.py`

```python
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class ClaimForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

#### `app/templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Expense Claims</title>
</head>
<body>
    <h1>Expense Claims</h1>
    <a href="{{ url_for('claim') }}">Submit a new claim</a>
    <ul>
        {% for claim in claims %}
            <li>{{ claim.description }} - {{ claim.amount }} - {{ claim.date }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `app/templates/claim.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <form action="" method="post">
        {{ form.hidden_tag() }}
        <p>
            {{ form.description.label }}<br>
            {{ form.description(size=32) }}<br>
            {% for error in form.description.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.amount.label }}<br>
            {{ form.amount(size=32) }}<br>
            {% for error in form.amount.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

#### `app/main.py`

```python
from app import app, db
from app.models import User, Claim

if __name__ == '__main__':
    app.run(debug=True)
```

### Running the Application

1. Ensure you have a database file (`expense_claims.db`) in the root directory.
2. Run the application using `python app/main.py`.

### Next Steps

1. **Authentication**: Implement user authentication using Flask-Login.
2. **Testing**: Add unit and integration tests.
3. **Styling**: Improve the web interface with CSS.
4. **Mobile App**: Develop a mobile app using Flutter or React Native.
5. **Deployment**: Deploy the application using Docker or a cloud service.

This project provides a basic structure for an expenses claim app, and you can expand it based on your requirements.