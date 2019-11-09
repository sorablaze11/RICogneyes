import requests
import json
import time
seconds = time.time()
# set to your own subscription key value
subscription_key = 'f42e427eee3343f182f3fe527d75a33a'
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v2.1/analyze'

image_url = 'https://wamu.org/wp-content/uploads/2019/08/IMG_4358-2-e1565263215111.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'visualFeatures': 'Categories,Description,Color,Objects'
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
print(json.dumps(response.json(), indent=4, sort_keys=True))

seconds1 = time.time()

print(seconds1 - seconds)