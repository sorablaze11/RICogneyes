# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import os
# from vision.facedet import face
import base64
from twilio.rest import Client
import requests
import json
import inflect
from django.templatetags.static import static
from gtts import gTTS
import geocoder
import random

universal_link = "https://fc5c29d2.ngrok.io"

def tts(payload):
    print("TTS Called")
    tts = gTTS(text=payload, lang='en')
    tts.save("/home/sorablaze/Desktop/Rakathon/RICogneyes/backend/staticfiles/audio.wav")
    tts.save("/home/sorablaze/Desktop/Rakathon/RICogneyes/backend/static/audio.wav")

def object(image_path):
    lst = []
    print("Object Called")
    subscription_key = 'f42e427eee3343f182f3fe527d75a33a'
    assert subscription_key
    image_data = open('/home/sorablaze/Desktop/Rakathon/RICogneyes/backend/static/some_image.png', "rb").read()
    # replace <My Endpoint String> with the string from your endpoint URL
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v2.1/analyze'
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}

    params = {
        'visualFeatures': 'Description,Objects',
    }

    response = requests.post(face_api_url, params=params,
                            headers=headers, data=image_data)
    #print(json.dumps(response.json(), indent=4, sort_keys=True))
    outputDict = eval(json.dumps(response.json()))
    #print(outputDict)
    #finalStr = outputDict['description']['captions'][0]['text'] + ". "
    lst.append(outputDict['description']['captions'][0]['text'] + ". ")
    #print(finalStr)
    obs = []
    for ob in outputDict['objects']:
        obs.append(ob['object'])
    
    uobs = set(obs)

    temp = "The objects in front of you are " 
    for ob in uobs:
        temp = temp + "," + ob + " " 
    lst.append(temp)
    #finalStr = finalStr + temp + '. '

    print(lst)
    return lst

def face(image_path):
    print("Face Called")
    p = inflect.engine()

    # set to your own subscription key value
    subscription_key = '324fb95616d349628daa880a79684ad2'
    assert subscription_key

    # replace <My Endpoint String> with the string from your endpoint URL
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    image_data = open(image_path, "rb").read()

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream'}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,emotion',
    }

    response = requests.post(face_api_url, params=params,headers=headers, data=image_data)
    #print(json.dumps(response.json(), indent=4, sort_keys=True))

    outputDict = eval(json.dumps(response.json()))

    numPeople = len(outputDict)

    finalStr = ""

    temp = str(numPeople) + " faces were detected in front of you."
    finalStr = finalStr + temp

    num = 1

    emoDic = {
        'anger' : 'angry',
        'contempt' : 'having contempt', 
        'disgust' : 'in disgust',
        'fear' : 'scared',
        'happiness' : 'happy',
        'neutral' : 'neutral',
        'sadness' : 'sad',
        'surprise' : 'surprised', 
    }

    for x in outputDict:
        gen = "She"
        if(x['faceAttributes']['gender'] == 'male'):
            gen = "He"

        emo = ""
        maxx = 0.0

        for y in x['faceAttributes']['emotion']:
            if( maxx < x['faceAttributes']['emotion'][y]):
                maxx = x['faceAttributes']['emotion'][y]
                emo = y

        print(emo)

        temp = " The " + p.ordinal(num) + " person is a " + x['faceAttributes']['gender'] + ". " + gen + " looks like " + gen + " is " + str(int(x['faceAttributes']['age'])) + " years old and is " + emoDic[emo] + ". "
        num += 1

        finalStr = finalStr + temp 

    print(finalStr)
    return finalStr

def ocr(imageUrl):
    url = "https://taggun.p.rapidapi.com/api/receipt/v1/verbose/url"
    #imageUrl = "https://courses.cs.vt.edu/csonline/AI/Lessons/VisualProcessing/OCRscans_files/robertson.jpg"
    payload = "{\"url\":\"" + imageUrl+ "\",\"headers\":{},\"refresh\":false,\"incognito\":false,\"ipAddress\":\"32.4.2.223\"}"
    headers = {
        'x-rapidapi-host': "taggun.p.rapidapi.com",
        'x-rapidapi-key': "b7f27d3d50mshd9bf5f0c086a683p136f85jsnc22917a3a34a",
        'content-type': "application/json",
        'accept': "application/json"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    output = json.loads(response.text)
    print(output)
    x = 'The text in front of you is :    ' + output['text']['text']
    print(x)
    return x


# Create your views here.
def clickImage(request):
    return render(request, 'index.html')

@csrf_exempt
def getAudio(request):
    encoded_image = request.POST.get('imgBase64')
    encoded_image = encoded_image.split(',')
    encoded_image = encoded_image[1]
    # print(encoded_image)
    missing_padding = len(encoded_image) % 4
    if missing_padding:
        print("Missing Padding")
        encoded_image += '=' * (4 - missing_padding)
    imgdata = base64.b64decode(encoded_image)
    filename = 'static/some_image.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata) 
    lst = object('/home/sorablaze/Desktop/Rakathon/RICogneyes/backend/static/some_image.png')
    tts(lst[0] + face('/home/sorablaze/Desktop/Rakathon/RICogneyes/backend/static/some_image.png') + lst[1])
    return JsonResponse({"filename":"/static/audio.wav"})

@csrf_exempt
def getNews(request):
    news = ['Maharashtra governor asks BJP to indicate willingness to form Government', 'Cyclone Bulbul news updates: Storm makes landfall, next 6 hours crucial for West Bengal', 'India briefs foreign heads of missions on Ayodhya verdict', 'Lord Ram became a party to the Ayodhya dispute']
    tts(random.choice(news))
    return JsonResponse({"filename":"/static/audio.wav"})

@csrf_exempt
def getSOS(request):
    g = geocoder.ip('me')
    print(g.latlng)
    mssg = "I'm in deep deep trouble." + "Latitute:" + str(g.latlng[0]) + ",Longitude:" + str(g.latlng[1])
    twilio_sid = "AC20cbc7110c48f924f0888e5704ebefbd"
    auth_token = "ae8a3bbb009a110ad817a4ec7a007c36"
    whatsapp_client = Client(twilio_sid, auth_token)
    contact_directory = {"Sukh Raj Limbu" : '+917358390216'}
    for key, value in contact_directory.items():
         msg_loved_ones = whatsapp_client.messages.create(
            body = mssg,
            from_= 'whatsapp:+14155238886',
            to='whatsapp:' + value,
        )
        # print(msg_loved_ones)
    tts('Distress message has been sent to you relatives and close ones through viber and whatsapp')
    return JsonResponse({"filename":"/static/audio.wav"})

@csrf_exempt
def getOCR(request):
    encoded_image = request.POST.get('imgBase64')
    encoded_image = encoded_image.split(',')
    encoded_image = encoded_image[1]
    # print(encoded_image)
    missing_padding = len(encoded_image) % 4
    if missing_padding:
        print("Missing Padding")
        encoded_image += '=' * (4 - missing_padding)
    imgdata = base64.b64decode(encoded_image)
    filename = 'static/some_image.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata) 
    lst = ocr(universal_link + '/static/some_image.png')
    tts(lst)
    return JsonResponse({"filename":"/static/audio.wav"})