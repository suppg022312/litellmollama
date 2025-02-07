Here's a Python script using the `outlook` library to access your Outlook calendar and send you reminders via email.

**Prerequisites:**

* You have an Outlook account with a Microsoft 365 subscription.
* You have the `requests`, `icalendar`, and `pywin32` libraries installed. You can install them via pip:

```bash
pip install requests icalendar pywin32
```

* Make sure you have enabled Calendars API for your Outlook account.

**Code:**
```python
import datetime
from icalendar import Calendar, Event
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your Outlook credentials
OUTLOOK_EMAIL = "your_outlook_email"
OUTLOOK_PASSWORD = "your_outlook_password"

# Email server settings for sending reminders
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
FROM_EMAIL = OUTLOOK_EMAIL
TO_EMAIL = OUTLOOK_EMAIL

def get_calendars():
    """Get a list of calendars from Outlook"""
    url = f"https://outlook.office365.com/ews/services.asmx?op=GetFolderByServer&ParentFolderClass=Scheduling"
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/xml; charset=utf-8"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["d"]["Folders"]
    else:
        raise Exception("Failed to retrieve calendars")

def get_meetings(calendars):
    """Get a list of upcoming meetings from the specified calendars"""
    meetings = []
    
    for calendar in calendars:
        url = f"https://outlook.office365.com/ews/services.asmx?op=GetItems&FolderId={calendar['d']['FolderId']}"
        headers = {
            "Authorization": f"Bearer {get_access_token()}",
            "Content-Type": "application/xml; charset=utf-8"
        }
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            for item in response.json()["d"]["Items"]:
                start_date = datetime.datetime.strptime(item["Start"], "%Y-%m-%dT%H:%M:%SZ")
                end_date = datetime.datetime.strptime(item["End"], "%Y-%m-%dT%H:%M:%SZ")
                
                if (datetime.datetime.now() - start_date).total_seconds() / 3600 < 24:
                    meetings.append({
                        "title": item["Subject"],
                        "start": start_date,
                        "end": end_date
                    })
        else:
            raise Exception("Failed to retrieve meetings")
    
    return meetings

def send_reminders(meetings):
    """Send reminders for each meeting"""
    for meeting in meetings:
        msg = MIMEMultipart()
        msg["Subject"] = f"Reminder: {meeting['title']}"
        msg["From"] = FROM_EMAIL
        msg["To"] = TO_EMAIL
        
        body = f"You have a meeting at {meeting['start'].strftime('%Y-%m-%d %H:%M')} - {meeting['end'].strftime('%Y-%m-%d %H:%M')}"
        msg.attach(MIMEText(body, "plain"))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        server.quit()

def get_access_token():
    """Get an access token for the Outlook API"""
    url = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "grant_type": "client_credentials"
    }
    
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://outlook.office.com/.default"
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception("Failed to retrieve access token")

def main():
    calendars = get_calendars()
    meetings = get_meetings(calendars)
    send_reminders(meetings)

if __name__ == "__main__":
    main()
```

**Note:**

* You'll need to replace the placeholders (`your_outlook_email`, `your_outlook_password`, etc.) with your actual Outlook credentials and email server settings.
* This script uses the `requests` library to interact with the Outlook API. Make sure you have the necessary permissions set up in the Azure portal for the Calendars API.
* The script sends reminders via email using the `smtplib` library.

Please let me know if you need any further assistance!