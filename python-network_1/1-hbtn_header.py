'''import requests packages installed in my local pc'''
import sys
import requests
url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)
print(response.headers['X-Request-Id'])
# ids=requests.requests_headers['x-Request-id']
