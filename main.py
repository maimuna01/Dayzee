# speech recognition AI Dayzee
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import cv2
import pyautogui
import time

engine = pyttsx3.init()  #initialize pyttsx3 module

client = wolframalpha.Client('your_address')  # wolfram client address

voices = engine.getProperty('voices')  # current value of engine property
engine.setProperty('voice', voices[len(voices) - 1].id)  # Queues command to set an engine property


class inout:
    def __init__(self):
        pass

    def speak(self, audio):
        print('Dayzee: ' + audio)
        engine.say(audio)
        engine.runAndWait()  # Makes speech audible in system

    def myCommand(self):
        r = sr.Recognizer()  # Uses Microphone
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1  # Seconds of non-speaking (no audio input)
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-in')
                print('User: ' + query + '\n')
            except sr.UnknownValueError:
                self.speak('Sorry Boss! I didn\'t get that! Try typing the command!')
                query = str(input('Command: '))

        return query


ipop = inout()  # class object
ipop.speak('Hello Boss, I am your digital assistant Dayzee!')
ipop.speak('Aapka dost.')
ipop.speak('How may i help you?')

# def TaskExecution():

if __name__ == "__main__":
    while True:
        query = ipop.myCommand();
        query = query.lower()

        if 'open youtube' in query:
            ipop.speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            ipop.speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            ipop.speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice & full of energy']
            ipop.speak(random.choice(stMsgs))

        elif 'email' in query:
            ipop.speak('Who is the recipient? ')
            recipient = ipop.myCommand()

            if 'me' in recipient:
                ipop.speak('What should I say? ')
                content = ipop.myCommand()

                server = smtplib.SMTP('smtp.gmail.com', 587)

                server.starttls()


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'exit' in query:
            ipop.speak('okay')
            ipop.speak('Bye Boss, have a good day.')
            sys.exit()

        elif 'hello' in query:
            ipop.speak('Hello Boss ')


        elif 'you can take rest' in query or 'now sleep' in query:
            ipop.speak('Okay sir, i am gonna sleep you can call me anytime. ')
            break

        elif 'play music' in query:
            music_folder = 'C:\\Users\\skt\\Music\\Youtube\\'
            music = ['Edison', 'bensound-actionable', 'bensound-buddy', 'Micro', 'Lucid_Dreamer']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            ipop.speak('okay, here is your music! Enjoy!')

        elif "take the screenshot" in query:
            ipop.speak("sir, please tell me the name for this screenshot file")
            name = query.lower()
            ipop.speak("please sir hold the screen for few seconds, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            ipop.speak("I am done sir, the screenshot is saved in our main folder.now i am ready!")


        elif "where are we" in query or "find my location" in query:
            ipop.speak("checking,Boss")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()  # go to json in the server
                city = geo_data['city']
                area = geo_data['area']
                country = geo_data['country']
                ipop.speak("Boss we are in {city} city of {area} area located in {country}")
            except Exception as e:
                ipop.speak("pardon Boss, due to network issue i am not able to find our location.")
                pass

        else:
            query = query
            ipop.speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    ipop.speak('Got it,')
                    ipop.speak('WOLFRAM-ALPHA says - ')
                    ipop.speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    ipop.speak('Got it, ')
                    ipop.speak('WIKIPEDIA says - ')
                    ipop.speak(results)

            except:
                webbrowser.open('www.google.com')

        ipop.speak('Next Command! Boss!')