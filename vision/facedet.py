import requests
import json
import inflect

def face():
    p = inflect.engine()

    # set to your own subscription key value
    subscription_key = '324fb95616d349628daa880a79684ad2'
    assert subscription_key

    # replace <My Endpoint String> with the string from your endpoint URL
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    image_url = 'https://cdn.collider.com/wp-content/uploads/2019/04/avengers-cast-interview-slice-600x200.jpg'

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,emotion',
    }

    response = requests.post(face_api_url, params=params,headers=headers, json={"url": image_url})
    #print(json.dumps(response.json(), indent=4, sort_keys=True))

    outputDict = eval(json.dumps(response.json()))

    numPeople = len(outputDict)

    finalStr = ""

    temp = "There are " + str(numPeople) + " people in front of you."
    finalStr = finalStr + temp

    num = 1

    emoDic = {
        'anger' : 'angry',
        'contempt' : 'contempt', 
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

        temp = " The " + p.ordinal(num) + " person is a " + x['faceAttributes']['gender'] + ". " + gen + " looks like " + gen + " is " + str(int(x['faceAttributes']['age'])) + " years old. " 
        temp = temp + gen + " is " + emoDic[emo] + ". "
        num += 1

        finalStr = finalStr + temp 

    print(finalStr)
    return finalStr