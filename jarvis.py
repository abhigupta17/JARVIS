import os
import random

import pyttsx3
from datetime import *
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good evening Sir!")
    speak("I'm jarvis,How may i help you sir?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print("Sorry! please say that again")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("seraching on  Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to Wikipedia")
            print(result)
            speak(result)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("Google.com")
        elif 'facebook' in query:
            webbrowser.open("facebook.com")
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        elif 'twitter' in query:
            webbrowser.open("twitter.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\DeLL\\Desktop\\songs1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'the time' in query:
            strtime = datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, The time is {strtime}")


