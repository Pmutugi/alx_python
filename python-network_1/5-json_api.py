import sys
import requests
''' imports from the modules'''
url = sys.argv[1]
q = "" if len(sys.argv) < 2 else sys.argv[2]
'''send data to the url'''
letter ={
    'q':q
}
'''post to the url'''
response = requests.post(url=url, data=letter)

try:
    json_response = response.json()
    if json_response:
        print("[{}] {}".format(json_response['id'],json_response['name']))
    else:
        print('No result')
except ValueError:
    print('Not a valid JSON')