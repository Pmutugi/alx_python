'''import requests packages installed in my local pc'''
import requests
'''define url as a variable that contains the actual url'''
url= 'https://alu-intranet.hbtn.io/status'
'''using the get method to get the url requests'''
response = requests.get(url)
print("Body response:")
print("\n -type:{}".format(type(url)))

print("\n -Content: OK".format(response.status_code))