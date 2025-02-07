To create such an AI agent you need to be familiar with Microsoft Graph API and Python.

Here is a basic example of how you could set up such an agent:

```python
import requests
from datetime import timedelta, datetime

# This function gets the upcoming meetings from your calendar.
def get_upcoming_meetings():
    # Get access token using client id and client secret
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'

    result = requests.post(
        "https://login.microsoftonline.com/your_tenant_name/oauth2/v2.0/token",
        data={
            'client_id': client_id,
            'scope': 'https://graph.microsoft.com/.default',
            'client_secret': client_secret,
            'grant_type': 'client_credentials'
        }
    )

    access_token = result.json()['access_token']

    # Get events from calendar
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    end_time = datetime.now() + timedelta(days=1)  # Get meetings for the next day

    response = requests.get(
        f"https://graph.microsoft.com/v1.0/users/{your_user_id}/calendarView?startdatetime={datetime_now()}&enddatetime={end_time}",
        headers=headers
    )

    return response.json().get('value', [])

# This function emails you about upcoming meetings.
def email_upcoming_meetings(meetings):
    for meeting in meetings:
        # Use an email service provider (like SendGrid) to send an email with the details of each meeting.

your_user_id = 'user-id'
meetings = get_upcoming_meetings()
email_upcoming_meetings(meetings)
```

Please replace placeholders (`'your_client_id'`, `'your_client_secret'`, `'your_tenant_name'`, `your_user_id`) with your actual data.

This program will check your Outlook calendar and email you in advance about any upcoming meetings. Note that this is a simplified example, you might need to expand it to suit your needs (like handling multiple users, meeting reminders, etc.). 

Remember this script uses client credentials flow for getting access token which provides app-only access to data without needing to sign-in a user.

Also note that the scope should be modified according to what kind of permissions you want to use from Microsoft Graph API. For accessing calendar data 'Calendars.Read' permission is required.
