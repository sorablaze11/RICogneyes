import requests
import json

def ocr(imageUrl):
    url = "https://taggun.p.rapidapi.com/api/receipt/v1/verbose/url"
    payload = "{\"url\":\"" + imageUrl+ "\",\"headers\":{},\"refresh\":false,\"incognito\":false,\"ipAddress\":\"32.4.2.223\"}"
    headers = {
        'x-rapidapi-host': "taggun.p.rapidapi.com",
        'x-rapidapi-key': "b7f27d3d50mshd9bf5f0c086a683p136f85jsnc22917a3a34a",
        'content-type': "application/json",
        'accept': "application/json"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    output = json.loads(response.text)
    print(output['text']['text'])
    #print('The text in front of you is :    ' + output['text'])

#imageUrl = "https://courses.cs.vt.edu/csonline/AI/Lessons/VisualProcessing/OCRscans_files/robertson.jpg"
#ocr(imageUrl)