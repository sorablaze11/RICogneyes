# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import os
import facedet
import base64

# Create your views here.
def clickImage(request):
    return render(request, 'index.html')

@csrf_exempt
def getDetails(request):
    encoded_image = request.POST.get('imgBase64')
    encoded_image = encoded_image.split(',')
    encoded_image = encoded_image[1]
    # print(encoded_image)
    missing_padding = len(encoded_image) % 4
    if missing_padding:
        print("Missing Padding")
        encoded_image += '=' * (4 - missing_padding)
    imgdata = base64.b64decode(encoded_image)
    filename = 'some_image.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata) 
    fname="audio.wav"
    # f = open(fname,"rb") 
    # response = HttpResponse()
    # response.write(f.read())
    # response['Content-Type'] ='audio/wav'
    # response['Content-Length'] =os.path.getsize(fname )
    return JsonResponse({"filename":fname})
