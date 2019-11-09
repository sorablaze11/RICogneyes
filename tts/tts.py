from gtts import gTTS

def tts(payload):
    tts = gTTS(text=payload, lang='en')
    tts.save("audio.wpa")

tts('There are 2 people in front of you. The 1st person is a female. She looks like She is 29 years old. She is neutral.  The 2nd person is a male. He looks like He is 45 years old. He is happy. . a group of people crossing a city street. The objects in front of you are ,person ,traffic light . ')