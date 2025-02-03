 Creating a Python agent to check Outlook emails involves using the Microsoft Graph API, which allows you to programmatically access Outlook email data. Below is a step-by-step guide to creating a Python agent that can check your Outlook emails.

### Prerequisites
1. **Azure AD App Registration**: You need to register an application in Azure Active Directory to get the necessary credentials (Client ID, Tenant ID, and Client Secret).
2. **Permissions**: Ensure your app has the necessary permissions to access Outlook email data. You need to set `Mail.Read` in the app registration.
3. **Install Required Libraries**: You will need the `requests` library to make HTTP requests and `msal` for handling authentication.

### Step-by-Step Guide

1. **Register an Application in Azure AD**:
   - Go to the Azure portal.
   - Navigate to Azure Active Directory.
   - Select "App registrations" and register a new application.
   - Note down the `Application (client) ID`, `Directory (tenant) ID`, and create a client secret.

2. **Install Required Libraries**:
   ```bash
   pip install requests msal
   ```

3. **Python Script**:
   ```python
   import requests
   import msal
   import json

   # Constants
   CLIENT_ID = 'your-client-id'
   TENANT_ID = 'your-tenant-id'
   CLIENT_SECRET = 'your-client-secret'
   SCOPE = ['https://graph.microsoft.com/.default']
   USER_EMAIL = 'your-email@example.com'

   # Authority
   AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

   # Initialize MSAL
   app = msal.ConfidentialClientApplication(
       CLIENT_ID,
       authority=AUTHORITY,
       client_credential=CLIENT_SECRET
   )

   # Get token
   result = app.acquire_token_for_client(scopes=SCOPE)

   if 'access_token' in result:
       token = result['access_token']
   else:
       print(result.get('error'))
       print(result.get('error_description'))
       print(result.get('correlation_id'))
       exit()

   # Headers
   headers = {
       'Authorization': f'Bearer {token}',
       'Content-Type': 'application/json'
   }

   # Get emails
   url = f'https://graph.microsoft.com/v1.0/users/{USER_EMAIL}/messages'
   response = requests.get(url, headers=headers)

   if response.status_code == 200:
       emails = response.json().get('value', [])
       for email in emails:
           print(f"Subject: {email.get('subject')}")
           print(f"From: {email.get('from').get('emailAddress').get('name')}")
           print(f"Received: {email.get('receivedDateTime')}")
           print(f"Body: {email.get('bodyPreview')}")
           print('-' * 50)
   else:
       print(f"Error: {response.status_code}")
       print(response.json())
   ```

### Explanation
1. **Authentication**:
   - **MSAL**: The `msal` library is used to acquire an access token using the client credentials flow.
   - **Client Credentials**: The application uses its own credentials (client ID, client secret) to authenticate.

2. **Fetching Emails**:
   - **Graph API**: The Microsoft Graph API is used to fetch emails. The endpoint `https://graph.microsoft.com/v1.0/users/{USER_EMAIL}/messages` retrieves emails for a specific user.
   - **Headers**: The access token is included in the request headers to authorize the request.

### Running the Script
1. **Set Environment Variables**: Set the environment variables for `CLIENT_ID`, `TENANT_ID`, `CLIENT_SECRET`, and `USER_EMAIL`.
2. **Run the Script**: Execute the script to see the emails in your Outlook inbox.

### Note
- Ensure that your Azure AD app has the necessary permissions (`Mail.Read`).
- The script uses a personal account. For work or school accounts, you might need to adjust the user email part of the URL.

This script provides a basic framework. Depending on your requirements, you might want to add error handling, logging, and other features.