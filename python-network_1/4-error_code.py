import sys
import requests
url = sys.argv[1]
response = requests.get(url=url)
if response.status_code >= 400:
    
    print ("Error code {}".format(response.status_code))
    
print(response.text)
