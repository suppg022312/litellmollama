Below is a basic Python script that utilizes the `pyautogui` library to open Outlook, navigate to your calendar, and use the `selenium` library to search for upcoming meetings and send you an email with the meeting details.

```python
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Email details
email_address = "your_email@gmail.com"
password = "your_password"

# Outlook details
outlook_username = "your_outlook_username"
outlook_password = "your_outlook_password"
outlook_server = "smtp.gmail.com"
outlook_port = 587

def check_meetings():
    # Set up the Outlook login credentials and connection details
    outlook_options = webdriver.ChromeOptions()
    outlook_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=outlook_options)
    
    # Navigate to the Outlook web interface
    driver.get("https://outlook.office.com/")
    
    # Enter the username and password
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i"))
    username_input.send_keys(outlook_username)
    username_input.send_keys(Keys.RETURN)
    
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "xLoginPassword")))
    password_input.send_keys(outlook_password)
    password_input.send_keys(Keys.RETURN)
    
    # Navigate to the calendar
    driver.get("https://outlook.office.com/inbox/calendar")
    
    # Find all upcoming meetings and send an email with their details
    current_time = datetime.now()
    for day in range(7):
        start_date = current_time + timedelta(days=day)
        end_date = start_date + timedelta(hours=24)
        
        meeting_dates = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ocCalendarViewDay")))
        meeting_dates = driver.find_elements(*meeting_dates)
        
        for meeting in meeting_dates:
            if start_date <= datetime.strptime(meeting.text, "%Y-%m-%d"):
                # Get the meeting title and time
                meeting_title = meeting.find_element(By.XPATH, ".//h1").text
                meeting_time = meeting.find_element(By.XPATH, ".//span[@class='ocTime']").text
                
                # Send an email with the meeting details
                message = "Subject: Upcoming Meeting - " + meeting_title + "\n\n"
                message += "Meeting Time: " + meeting_time
                
                # Attach the calendar invitation to the email body
                message += "\n\nCalendar Invitation: https://outlook.office.com/invitations/" + start_date.strftime("%Y%m%dT%H%M%SZ") + "/?path=" + start_date.strftime("%Y%m%dT%H%M%SZ")
                
                # Send the email using the Gmail API
                import smtplib
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                
                server = smtplib.SMTP(outlook_server, outlook_port)
                server.starttls()
                server.login(email_address, password)
                msg = MIMEMultipart()
                msg["From"] = email_address
                msg["To"] = "recipient_email@gmail.com"
                msg["Subject"] = "Upcoming Meeting - " + meeting_title
                body = message
                msg.attach(MIMEText(body, "plain"))
                text = msg.as_string()
                server.sendmail(email_address, "recipient_email@gmail.com", text)
                server.quit()

check_meetings()
```

This script uses the `selenium` library to open Outlook and navigate to your calendar. It then searches for all upcoming meetings within the next 7 days. For each meeting, it extracts the title and time and sends an email with these details.

You'll need to replace the placeholders (`your_email`, `your_password`, etc.) with your actual Outlook login credentials and email address.

Please note that this script is just a basic example and might not work for everyone due to differences in how Outlook handles meeting invitations and emails. You may need to modify it to suit your specific needs.

Also, keep in mind that this script will send an email for every day with meetings scheduled. If you don't want to receive multiple emails per day, you'll need to modify the script to filter out non-meeting days.

Lastly, if you're using Gmail as your Outlook provider, make sure to enable "Less secure app access" in your account settings before running this script.