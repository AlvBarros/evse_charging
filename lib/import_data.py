import requests
import json

# Set data for request
endpoint='https://hgy780tcj2.execute-api.eu-central-1.amazonaws.com/dev/data'
headers = {'Authentication1': 'Basic interviewee:muchpassword'}

def importSupplierPricesData():
    print('Retrieving data...')
    # HTTP GET Request to specified endpoint with specified headers
    response = requests.get(endpoint, headers=headers)

    # Return data only if request was successful (status code returns 200)
    if (response.status_code != 200):
        print('Failed to retrieve data')
        status='Status code: ' + str(response.status_code)
        respns='Response text: ' + str(response.text)
        raise Exception(status+'\n'+respns)
    else:
        print('Retrieved data successfully')
        return json.loads(response.text.lower())

# PS: I didn't find it important to create auth and URL files
# only for a single HTTP request, but I recognize that
# it would be much more scalable and maintainable