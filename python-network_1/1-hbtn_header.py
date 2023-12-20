'''import requests packages installed in my local pc'''
import sys
import requests
url = input('Enter URL: ') if len(sys.argv) < 2 else sys.argv[1]
'''returning the response from the server'''
response = requests.get(url)
if 'X-Request-Id' in response.headers:
    value = response.headers['X-Request-Id']
    print(value)

