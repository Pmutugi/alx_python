#Python script that takes your GitHub credentials (username and password)
# use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
import sys
import requests

from requests.auth import HTTPBasicAuth
username= sys.argv[1]
access_token = sys.argv[2]
response =requests.get(url=username, auth=HTTPBasicAuth(username, access_token))
try:
     if response.status_code==200:
         user_credentials =response.json()
         print(user_credentials['id'])
     else:
        print('None')
except ValueError:
     print('None')