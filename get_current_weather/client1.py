import http.client

conn = http.client.HTTPSConnection

("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"

req,
    'x-rapidapi-key': "80206ff78emsh043d326d6426004p155e9ejsn0eb2613374d3"
    }

conn.request("GET", "/weather?callback=test&id=2172797&units=%22metric%22%20or%20%22imperial%22&mode=xml%2C%20html&q=London%2Cuk", headers=

reqheaders)

res = conn.getresponse()

req
data = res.read()

print(data

req.decode("utf-8"))

	


req

	