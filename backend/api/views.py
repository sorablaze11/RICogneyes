# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import os
# from vision.facedet import face
import base64

import requests
import json
import inflect
from django.templatetags.static import static
from gtts import gTTS

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

# Create your views here.
def clickImage(request):
    return render(request, 'index.html')

@csrf_exempt
def getAudio(request):
    url = static('audio.wav')
    print(url)
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
    tts('Fake News')
    return JsonResponse({"filename":"/static/audio.wav"})

@csrf_exempt
def getSOS(request):
    tts('Fake Distress Call')
    return JsonResponse({"filename":"/static/audio.wav"})

@csrf_exempt
def getOCR(request):
    tts('Fake Optical Character Recognition Call')
    return JsonResponse({"filename":"/static/audio.wav"})