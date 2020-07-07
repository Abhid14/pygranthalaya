"""
def _speak(sentence):
	with tempfile.NamedTemporaryFile(delete=True) as fp:
		tts = gTTS(text=sentence, lang='en')
		tts.save(os.path.join(config.data_dir, '{}.mp3'.format(fp.name)))
		mixer.music.load(os.path.join(config.data_dir, '{}.mp3'.format(fp.name)))
		mixer.music.play()
"""
import speech_recognition as sr # recognise speech
"""import playsound # to play an audio file
from gtts import gTTS # google text to speech"""
import webbrowser # open browser
"""import ssl
import certifi"""
import tempfile
import time
import os # to remove created audio files
#from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
#import bs4 as bs
#import urllib.request

from pygame import mixer 
"""  
# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("naivety.mp3") 
  
# Setting the volume 
mixer.music.set_volume(1.0) 
  
# Start playing the song 
mixer.music.play() 
  
# infinite loop 
while True: 
      
    print("Press 'p' to pause, 'r' to resume") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
      
    if query == 'p': 
  
        # Pausing the music 
        mixer.music.pause()      
    elif query == 'r': 
  
        # Resuming the music 
        mixer.music.unpause() 
    elif query == 'e': 
  
        # Stop the mixer 
        mixer.music.stop() 
        break"""
r = sr.Recognizer()
with sr.Microphone() as source:
	print('Kuch bhauk')
	audio = r.listen(source)
	voice_data = r.recognize_google(audio)
	print(voice_data)