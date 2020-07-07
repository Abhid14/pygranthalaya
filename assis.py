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

