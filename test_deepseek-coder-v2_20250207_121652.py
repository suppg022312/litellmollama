 To create an AI agent that checks your Outlook calendar for upcoming meetings and emails you a reminder, you'll need to use the Microsoft Graph API with Python. Below is a step-by-step guide on how to set up this script using the `msal` library for authentication and the `python-dateutil` library to handle dates and times.

### Prerequisites:
1. **Python**: Ensure you have Python installed on your machine.
2. **Microsoft 365 Account**: You need a Microsoft 365 account with Outlook enabled.
3. **Azure App Registration**: Register an application in Azure Active Directory to get the client ID, tenant ID, and client secret.
4. **Permissions**: The app must have `Calendars.Read` permissions.

### Steps:
1. **Install Required Libraries**:
   ```bash
   pip install msal python-dateutil
   ```

2. **Create a Python Script**:
   Here's a complete script to check your Outlook calendar and send an email reminder for upcoming meetings:

```python
import os
import datetime
import requests
import json
from msal import ConfidentialClientApplication
from dateutil import parser, tz
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

# Azure AD app registration details
CLIENT_ID = 'your-client-id'
TENANT_ID = 'your-tenant-id'
CLIENT_SECRET = 'your-client-secret'
USER_EMAIL = 'your-email@example.com'  # The email address of the account you want to check
SCOPES = ['https://graph.microsoft.com/Calendars.Read']
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

# Initialize MSAL app
app = ConfidentialClientApplication(CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET)

# Get access token
result = app.acquire_token_for_client(scopes=SCOPES)
if 'access_token' in result:
    ACCESS_TOKEN = result['access_token']
else:
    print("Could not acquire token")
    exit()

# Function to get upcoming meetings
def get_upcoming_meetings():
    url = f"https://graph.microsoft.com/v1.0/users/{USER_EMAIL}/calendar/events"
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['value']
    else:
        print("Failed to get events:", response.status_code, response.text)
        return []

# Function to send email
def send_email(meeting):
    smtp_server = 'smtp.office365.com'  # Use your SMTP server details
    port = 465  # SSL port for Office 365
    sender_email = USER_EMAIL
    recipient_email = USER_EMAIL
    password = 'your-email-password'  # Password or app-specific password if you use two-factor auth

    msg = MIMEText(f"Meeting '{meeting['subject']}' is upcoming at {meeting['start']['dateTime']}.")
    msg['Subject'] = f"Reminder: Meeting '{meeting['subject']}'"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, [recipient_email], msg.as_string())

# Main function to check and send reminders
def main():
    meetings = get_upcoming_meetings()
    for meeting in meetings:
        start_time = parser.isoparse(meeting['start']['dateTime'])
        current_time = datetime.datetime.now(tz.gettz('UTC'))
        if start_time > current_time + datetime.timedelta(hours=1):  # Send reminder 1 hour before the meeting
            print("Meeting:", meeting['subject'], "is upcoming.")
            send_email(meeting)

if __name__ == "__main__":
    main()
```

### Explanation:
- **Authentication**: Uses MSAL to authenticate with Microsoft Graph API.
- **Fetching Events**: Retrieves events from the user's calendar using the `/users/{user_id}/calendar/events` endpoint.
- **Sending Emails**: Sends an email reminder for each upcoming meeting, configured to send 1 hour before the event start time.

### Notes:
- Replace placeholders (like `your-client-id`, `your-tenant-id`, etc.) with your actual Azure AD registration details and user credentials.
- Ensure that you have set up two-factor authentication for your Microsoft account if using a personal email address, as it won't work without an app password.
- Adjust the script based on your specific requirements or environment (e.g., handling different time zones).

This script provides a basic framework and can be extended with more features like logging, error handling, etc.