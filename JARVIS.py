import random

import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random
webbrowser.register("chrome",None)

engine=pyttsx3.init("sapi5")
voice=engine.getProperty("voices")
# print(voice[1].id)
engine.setProperty("voice",voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hours=int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak("Good morning Sandeep Sir")
    elif hours>=12 and hours<=18:
        speak("Good afternoon Sandeep Sir")
    else:
        speak("Good evening Sandeep sir")
    speak("I am gaurav your personal assistant . How may i help you ")

def take_commad():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold =1
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said {query}")

    except Exception as e:
        print("Say that again please")
        return "NONE"
    return query


if __name__ == "__main__":
    wishme()
    query=take_commad().lower()
    if "wikipedia" in query:
        print("Searching Wikipedia")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")

    elif "play music" in query:
        music_dir="G:\\hp today data backup\\local disk d\\SHAREit\\audios\\Download"
        songs=os.listdir(music_dir)
        random_songs=random.randint(0,len(songs))
        os.startfile(os.path.join(music_dir,songs[random_songs]))

    elif "google news" in query:
        webbrowser.open("googlenews.com")

    elif "the time" in query:
        srttime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {srttime}")

    elif "sing happy birthday" in  query:
        happy_dir="C:\\Users\\intel\\Documents\\happy Birthday"
        song=os.listdir(happy_dir)
        os.startfile(os.path.join(happy_dir,song[0]))