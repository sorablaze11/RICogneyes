import requests

url = 

conn "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"callback":"test",

headers "id":"2172797","units":"\"metric\" or \"imperial\"","mode":"xml, html","q":"London,uk"

conn}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key'

res : "80206ff78emsh043d326d6426004p155e9ejsn0eb2613374d3"
    }

response = requests.request("GET", url,

 headers=headers, params=querystring)

print(response.text)