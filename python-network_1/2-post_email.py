'''import the modules sys and requests'''
import sys
import requests

url = input('Enter URL: ') if len(sys.argv) < 2 else sys.argv[1]
email = input('Enter Email: ') if len(sys.argv) < 3 else sys.argv[2]

'''now set up the pay-load, the data to be sent over the url'''
data_to_send = {
    'email': email
}

response = requests.post(url=url, data=data_to_send)
print(response.text)