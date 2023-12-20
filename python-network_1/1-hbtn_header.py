'''import requests packages installed in my local pc'''
import sys
import requests
# url = 'https://alu-intranet.hbtn.io/status'
# response = requests.get(url[id])
# for id, argv in enumerate(id, response):
   
# import requests
# import sys
'''to check to compliance of the condition of the id with the url get method'''
def get_request_id(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the value of the X-Request-Id header from the response
            request_id = response.headers.get('X-Request-Id')

            # Display the value of the X-Request-Id header
            print("{}".format({request_id}))
        else:
            print("{}".format({response.status_code}))

    except requests.RequestException as e:
        print({e})

# if __name__ == "__main__":
#     # Check if a URL is provided as a command-line argument
#     if len(sys.argv) != 2:
#         print("Usage: python script.py <URL>")
#         sys.exit(1)

#     url = sys.argv[1]
#     get_request_id(url)