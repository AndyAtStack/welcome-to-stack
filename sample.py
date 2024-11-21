import requests
from requests_oauthlib import OAuth2Session
import webbrowser

# 1. Your AwardWallet API credentials (replace these with your actual credentials)
CLIENT_ID = sails  # Your client ID
CLIENT_SECRET = R7dxaLfza67cYdvqaUZ2ihR8XkmnM  # Replace with your actual client secret
REDIRECT_URI = 'https://andyatstack.github.io/welcome-to-stack/'  # Your registered redirect URI
SCOPE = 'read'  # Replace with the actual scope if needed
AUTHORIZATION_URL = 'https://business.awardwallet.com/api/oauth/authorize'
TOKEN_URL = 'https://business.awardwallet.com/api/oauth/token'
API_ENDPOINT = 'https://business.awardwallet.com/api/provider/list'  # Replace with the actual API endpoint you want to access

# 2. Set up OAuth2Session
oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)

# 3. Generate the authorization URL and print it for the user to visit
authorization_url, state = oauth.authorization_url(AUTHORIZATION_URL)

# 4. Direct the user to the authorization URL for them to log in and authorize your app
print(f"Please go to this URL and authorize access: {authorization_url}")
webbrowser.open(authorization_url)  # This will open the URL in the default web browser automatically

# 5. After user authorizes, they will be redirected back to your REDIRECT_URI with a 'code' parameter
# The user needs to copy and paste the full redirect URL here
redirect_response = input("Paste the full redirect URL here: ")

# 6. Exchange the authorization code for an access token
oauth.fetch_token(TOKEN_URL, authorization_response=redirect_response, client_secret=CLIENT_SECRET)

# 7. Now you can use the access token to make authorized API requests
response = oauth.get(API_ENDPOINT)

# 8. Check the response and handle it
if response.status_code == 200:
    print("Data fetched successfully.")
    print(response.json())  # Print the JSON response from the API
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.text)  # Print the error message returned by the API

