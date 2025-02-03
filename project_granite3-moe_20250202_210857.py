1. First, let's create a user interface using Django, a Python web framework. We'll need to create several models for our expense categories, users, and transactions.

```python
# In /src/accounts/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Transaction(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
```

2. Next, we'll create a user authentication system using Django's built-in authentication system. We'll need to create a User model and a password reset view.

```python
# In /src/accounts/models.py
from django.contrib.auth import checks.EmailAuthRequired
from django.contrib.auth.models import User

class PasswordResetForm(UserCreationForm):
    email = forms.CharField(required=False, upload_to_directory=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form._errors['email'] = forms.UserError('email')

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = False
            user.save()
            return HttpResponseRedirect('/make-password-reset-token/')
    else:
        form = PasswordResetForm()

    return render(request, 'accounts/password_reset.html', {'form': form})
```

3. We'll create a view to handle the password reset process and send a token to the user's email.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from .forms import PasswordResetForm
from django.contrib.auth.hashers import make_password

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = False
            user.save()
            send_password_reset_email(user, request.HttpContext.request.META['HTTP_X_REQUESTED_WITH'])
            return redirect('home')
    else:
        form = PasswordResetForm()

    return render(request, 'accounts/password_reset.html', {'form': form})
```

4. We'll create a view to send the password reset email and handle the token expiration.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from .forms import PasswordResetForm
from django.contrib.auth.mail.handlers import EmailNotificationHandler
from django.contrib.auth.models import User
import time

def send_password_reset_email(user, token):
    # Set up email parameters
    to_email = user.email
    subject = 'Your account has been reset'
    msg_content = f"Dear {user.username},\n\nThis is a test password reset email.\n\nPlease change your password at https://yourwebsite.com."

    # Set up the email handler
    handler = EmailNotificationHandler(to_email, subject, msg_content)

    # Schedule the email to be sent after some time
    schedule.every().day.at("09:00").do(handler)

    return
```

5. Finally, we'll create a view to handle the password reset confirmation and update the user's password.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import time

def password_reset_confirmation(request, token):
    user = User.objects.get(username=request.user.username)
    user.set_password(make_password(user.password))
    user.save()

    # Schedule the email to be sent after some time
    schedule.every().day.at("09:00").do(handler)

    return render(request, 'accounts/password_reset_confirmation.html', {'user': user})
```

6. Create a view to handle the password reset confirmation and send the email.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.mail.handlers import EmailNotificationHandler
from django.contrib.auth.models import User
import time

def password_reset_confirmation(request, token):
    user = User.objects.get(username=request.user.username)
    user.set_password(make_password(user.password))
    user.save()

    # Schedule the email to be sent after some time
    schedule.every().day.at("09:00").do(handler)

    return render(request, 'accounts/password_reset_confirmation.html', {'user': user})
```

7. Create a view to handle the password reset confirmation and send the email.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.mail.handlers import EmailNotificationHandler
from django.contrib.auth.models import User
import time

def password_reset_confirmation(request, token):
    user = User.objects.get(username=request.user.username)
    user.set_password(make_password(user.password))
    user.save()

    # Schedule the email to be sent after some time
    schedule.every().day.at("09:00").do(handler)

    return render(request, 'accounts/password_reset_confirmation.html', {'user': user})
```

8. Create a view to handle the password reset confirmation and send the email.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.mail.handlers import EmailNotificationHandler
from django.contrib.auth.models import User
import time

def password_reset_confirmation(request, token):
    user = User.objects.get(username=request.user.username)
    user.set_password(make_password(user.password))
    user.save()

    # Schedule the email to be sent after some time
    schedule.every().day.at("09:00").do(handler)

    return render(request, 'accounts/password_reset_confirmation.html', {'user': user})
```

9. Create a view to handle the password reset confirmation and send the email.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.mail.handlers import EmailNotificationHandler
from django.contrib.auth.models import User
import time

def password_reset_confirmation(request, token):
    user = User.objects.get(username=request.user.username)
    user.set_password(make_password(user.password))
    user.save()

    # Schedule the email to be sent after some time
    schedule.every().day.at("09:00").do(handler)

    return render(request, 'accounts/password_reset_confirmation.html', {'user': user})
```

10. Create a view to handle the password reset confirmation and send the email.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.mail.handlers import EmailNotificationHandler
from django.contrib.auth.models import User
import time

def password_reset_confirmation(request, token):
    user = User.objects.get(username=request.user.username)
    user.set_password(make_password(user.password))
    user.save()

    # Schedule the email to be sent after some time
    schedule.every().day.at("09:00").do(handler)

    return render(request, 'accounts/password_reset_confirmation.html', {'user': user})
```

11. Create a view to handle the password reset confirmation and send the email.

```python
# In /src/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.mail.handlers import EmailNotificationHandler
from django.contrib.auth.models import User
import time

def password_reset_confirmation(request, token):
    user = User.objects.get(