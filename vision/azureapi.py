import requests
import json
import time
seconds = time.time()

seconds = time.time()

# set to your own subscription key value
subscription_key = '324fb95616d349628daa880a79684ad2'
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

image_url = 'https://wamu.org/wp-content/uploads/2019/08/IMG_4358-2-e1565263215111.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,emotion',
}

response = requests.post(face_api_url, params=params,headers=headers, json={"url": image_url})
print(json.dumps(response.json()))

seconds1 = time.time()

print(seconds1 - seconds)