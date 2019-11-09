url 

querystring response = unirest.get("https://community-open-weather-map.p.rapidapi.com/weather?callback=test&id=2172797&units=%22metric%22+or+%22imperial%22&mode=xml%2C+html&q=London%2Cuk",
  headers={
    "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
    "X-RapidAPI-Key": "80206ff78emsh043d326d6426004p155e9ejsn0eb2613374d3"
  }
)

headers 

response 