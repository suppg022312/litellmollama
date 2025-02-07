To create an AI agent that checks your Outlook calendar for upcoming meetings and sends you emails in advance, we'll use the following libraries:

1. `requests` to interact with Microsoft Graph API
2. `datetime` to handle date and time calculations
3. `email` to send emails using a Gmail account (you can use any email service that supports SMTP)

Please note that this code requires you to have an Outlook account, as well as a Microsoft Azure AD application registered in the Azure portal with the necessary permissions.

**Step 1: Register your Azure AD Application**

1. Go to the Azure portal and register a new application.
2. In the "API permissions" section, add the following permissions:
	* `https://graph.microsoft.com/.default`
	* `Calendars.Read`
	* `Mail.Send`
3. Note down the Client ID, Tenant ID, and Client Secret.

**Step 2: Install required libraries**

```bash
pip install requests
```

**Step 3: Create a Python script using the following code**

```python
import requests
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Outlook account credentials
OUTLOOK_USERNAME = 'your_outlook_username@outlook.com'
OUTLOOK_PASSWORD = 'your_outlook_password'

# Microsoft Graph API credentials
AZURE_CLIENT_ID = 'your_client_id'
AZURE_TENANT_ID = 'your_tenant_id'
AZURE_CLIENT_SECRET = 'your_client_secret'

# Gmail account credentials for sending emails (optional)
GMAIL_USERNAME = 'your_gmail_username@outlook.com'
GMAIL_PASSWORD = 'your_gmail_password'

def get_token():
    auth_url = f'https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/v2.0/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': AZURE_CLIENT_ID,
        'client_secret': AZURE_CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default',
    }
    response = requests.post(auth_url, headers=headers, data=data)
    return response.json()['access_token']

def get_calendar_events(access_token):
    graph_url = 'https://graph.microsoft.com/v1.0/me/events'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    response = requests.get(graph_url, headers=headers)
    return response.json()['value']

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USERNAME
    msg['To'] = OUTLOOK_USERNAME
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(GMAIL_USERNAME, OUTLOOK_USERNAME, text)
    server.quit()

def main():
    access_token = get_token()
    events = get_calendar_events(access_token)

    for event in events:
        start_time = datetime.datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        end_time = datetime.datetime.strptime(event['end']['dateTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if (datetime.datetime.now() - start_time).total_seconds() / 3600 < 24:
            subject = f'Meeting reminder: {event["subject"]}'
            body = f'You have a meeting with {event["attendees"][0]["emailAddress"]["address"]} on {start_time.strftime("%Y-%m-%d %H:%M")}.'
            send_email(subject, body)

if __name__ == '__main__':
    main()
```

**Step 4: Run the script**

Save this code in a file (e.g., `outlook_calendar_agent.py`) and run it using Python:

```bash
python outlook_calendar_agent.py
```

This will check your Outlook calendar for upcoming meetings within the next 24 hours and send you an email reminder for each meeting.

Please note that this is just a basic example, and you may want to modify it to suit your specific needs. Additionally, be sure to handle any errors that might occur during execution.