url 

querystring import http.client

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key':

headers 

response 

 "80206ff78emsh043d326d6426004p155e9ejsn0eb2613374d3"
    }

conn.request("GET", "/forecast/daily?q=san%20francisco%2Cus&lat=35&lon=139&cnt=10&units=metric%20or%20imperial", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))