import requests
import json
subscription_key = 'f42e427eee3343f182f3fe527d75a33a'
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v2.1/analyze'

image_url = 'https://wamu.org/wp-content/uploads/2019/08/IMG_4358-2-e1565263215111.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'visualFeatures': 'Description,Objects',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
#print(json.dumps(response.json(), indent=4, sort_keys=True))
outputDict = eval(json.dumps(response.json()))
#print(outputDict)
finalStr = outputDict['description']['captions'][0]['text'] + ". "

#print(finalStr)
obs = []
for ob in outputDict['objects']:
    obs.append(ob['object'])
   
uobs = set(obs)

temp = "The objects in front of you are " 
for ob in uobs:
    temp = temp + "," + ob + " " 

finalStr = finalStr + temp + '. '

print(finalStr)