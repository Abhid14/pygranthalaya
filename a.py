import speech_recognition as sr
import io
from pygame import mixer 
import os
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        engine.say('Please say something')
        engine.runAndWait()
        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")


        # recognize speech using google

        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")


        except Exception as e:
            print("Error :  " + str(e))
while True:
    if __name__ == "__main__":
        main()