'''import requests packages installed in my local pc'''
import sys
import requests
url = input("input your url:")

ids=requests.headers['x-Request-id']

print(ids) 