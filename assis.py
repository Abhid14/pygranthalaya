import speech_recognition as sr

def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")


        # recognize speech using google

        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")


        except Exception as e:
            print("Error :  " + str(e))




        # write audio

        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
while True:
	if __name__ == "__main__":
		main()

"""import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
    except:
        print("Sorry could not recognize what you said")
print(text)"""