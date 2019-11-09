import requests
import json

response = requests.post("https://summarize-text.p.rapidapi.com/",
  headers={
    "X-RapidAPI-Host": "summarize-text.p.rapidapi.com",
    "X-RapidAPI-Key": "b7f27d3d50mshd9bf5f0c086a683p136f85jsnc22917a3a34a",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  params={
    "minimum": 1,
    "maximum": 1,
    "text": "The Supreme Court's judgement in the Ayodhya case will shape the political and social landscape of India, the US media reported on Saturday, noting the steps taken by the Indian government to maintain law and order in the country after the verdict. The apex court in a unanimous verdict on Saturday cleared the way for the construction of a Ram Temple at the disputed site at Ayodhya, and directed the Centre to allot a 5-acre plot to the Sunni Waqf Board for building a mosque. In one of the most important and most anticipated judgements in India's history, a five-judge Constitution bench headed by Chief Justice Ranjan Gogoi put an end to the more than a century old dispute that has torn the social fabric of the nation. For all the case's historical origins, its judgment will help shape India's political and social landscape, The Wall Street Journal, which has been following the case closely, said in a news dispatch from New Delhi. Most of the mainstream American media, which reported about the verdict, underscored that the ruling by the five-judge bench led by Chief Justice of India Ranjan Gogoi was unanimous. It also noted the steps taken by the government to maintain law and order in the country and across the board for overall acceptance of the apex court's judgement in this regard. The Union home ministry kept a constant and engaging vigil across the country with central paramilitary forces, intelligence agencies and state police forces in toe."
  }
)


output = json.loads(response.text)
print("Today's News short reads:     ")
print(*output['summary'], sep = "\n")


