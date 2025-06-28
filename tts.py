from gtts import gTTS
from playsound import playsound
import os

text = "type whatever you want"
print("making...")
tts = gTTS(text=text, lang='en') 
filename = "output.mp3"
tts.save(filename)
print("file saved, playing sound")  
playsound(filename)  