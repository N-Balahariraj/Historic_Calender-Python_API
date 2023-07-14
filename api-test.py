import requests
#API_KEY = "UbVZej3yrHJV+ecO+rxMsQ==oo0aKI49HPbUciVP"
text = 'roman empire'
api_url = 'https://api.api-ninjas.com/v1/historicalevents?text={}'.format(text)
response = requests.get(api_url, headers={'X-Api-Key': 'UbVZej3yrHJV+ecO+rxMsQ==oo0aKI49HPbUciVP'})

print(response.status_code)

event= response.json()[3]['event']
year= response.json()[3]['year']

print(event)
print( "{}BC".format((abs(int(year)))))