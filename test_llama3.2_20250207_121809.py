Below is a simple implementation of an AI agent using Python that checks your Outlook calendar for upcoming meetings and sends you emails with the details.

```python
import pyautogui
import datetime
from email.message import EmailMessage
import smtplib
from imaplib import IMAP4
import imaplib

# Set up Outlook account credentials (replace with your own)
OUTLOOK_ACCOUNT = 'your-outlook-account'
OUTLOOK_PASSWORD = 'your-outlook-password'

# Function to connect to Outlook account and check calendar for upcoming meetings
def check_outlook_calendar():
    # Connect to Outlook account using IMAP4
    imap = IMAP4_SSL('imap mail.microsoft.com')
    imap.login(OUTLOOK_ACCOUNT, OUTLOOK_PASSWORD)
    
    # Select the Inbox folder
    imap.select('Inbox')
    
    # Search for emails with subject containing "Meeting" or "Event"
    status, messages = imap.search(None, '(SUBJECT "Meeting" OR SUBJECT "Event")')
    
    # Iterate over email IDs and get email details
    for num in messages[0].split():
        status, msg = imap.fetch(num, '(RFC822)')
        raw_email = msg[0][1]
        
        # Parse the email using EmailMessage
        email_message = EmailMessage()
        email_message.decode_content = True
        email_message.add_header('Subject', raw_email.get('Subject'))
        email_message.set_content(raw_email.get_content())
        
        # Get the meeting start and end times
        start_time = datetime.datetime.strptime(email_message['subject'].split(' - ')[1], '%Y-%m-%d %H:%M')
        end_time = datetime.datetime.strptime(email_message['subject'].split(' - ')[2], '%Y-%m-%d %H:%M')
        
        # Send email with meeting details
        send_email(start_time, end_time)

# Function to send email with meeting details
def send_email(start_time, end_time):
    # Set up Gmail account credentials (replace with your own)
    from_account = 'your-gmail-account'
    to_account = 'your-email-address'
    
    # Create a new email message
    msg = EmailMessage()
    msg['From'] = from_account
    msg['To'] = to_account
    
    # Set the subject and body of the email
    msg.set_content(f'Meeting: {start_time.strftime("%A, %B %d, %Y at %I:%M %p")}\n'
                    f'Location: {email_message.get('Subject').split(' - ')[1]}\n'
                    f'Duration: {(end_time-start_time).total_seconds() // 3600} hours')
    
    # Send the email using Gmail account
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_account, 'your-gmail-password')
    server.send_message(msg)
    server.quit()

# Call the function to check Outlook calendar for upcoming meetings
check_outlook_calendar()
```

Please note that you need to replace `your-outlook-account`, `your-outlook-password`, `your-gmail-account` and `your-gmail-password` with your actual Outlook account credentials and Gmail account credentials.

Also, please be aware of the security implications of using email services for scheduling meetings. This script is just a basic example and may not work perfectly in all cases.

You can also consider adding more features to this script such as:

*   Handling multiple calendars
*   Dealing with different time zones
*   Sending reminders before each meeting