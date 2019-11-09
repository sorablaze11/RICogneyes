from gtts import gTTS

def tts(payload):
    tts = gTTS(text=payload, lang='en')
    tts.save("audio.wpa")

tts('hello sukh raj limbu')