import requests


mon = 6
day = 12
api_url = "https://api.api-ninjas.com/v1/historicalevents?month={}&day={}".format(
    mon, day
)
response = requests.get(
    api_url, headers={"X-Api-Key": "UbVZej3yrHJV+ecO+rxMsQ==oo0aKI49HPbUciVP"}
)
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)


# print("\n",type(response))
# print("\n",(response.status_code))
