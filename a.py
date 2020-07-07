import speech_recognition as sr
import io
from pygame import mixer 
import os
import pyttsx3
# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("naivety.mp3") 
  
# Setting the volume 
mixer.music.set_volume(1.0) 
  
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        mixer.music.play() 
        engine.say('Please say something')
        engine.runAndWait()
        print("Please say something")

        audio = r.listen(source)
        print("Recognizing Now .... ")
        mixer.music.play()

        # recognize speech using google

        try:
            engine.say("You have said \n" + r.recognize_google(audio))
        except Exception as e:
            print("Error :  " + str(e))
while True:
    if __name__ == "__main__":
        main()