url 

querystring import requests

url = 

conn "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

querystring = {"q":"san francisco,us",

headers "lat":"35","lon":"139","cnt":"10","units"

headers 

response 

:"metric or imperial"

conn}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key'

res : "80206ff78emsh043d326d6426004p155e9ejsn0eb2613374d3"
    }

response = requests.request("GET", url,

 headers=headers, params=querystring)

print(response.text)