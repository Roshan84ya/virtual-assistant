#-------------------------------------------------------
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import smtplib

#--------------------------------------------------------
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
MYNAME='Roshan'
#--------------------------------------------------------
#this function will speak what pe pass into it
def speak(text):
    engine.say(text)
    engine.runAndWait()
#---------------------------------------------------------
#this function will wish you
def wishme(MYNAME):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morining {}".format(MYNAME))
    elif hour>=12 and hour<18:
        speak("Goof AfterNoon {}".format(MYNAME))
    else:
        speak("Goof Evening {}".format(MYNAME))
    #speak("Good How may i help you {} ".format(MYNAME))
#-----------------------------------------------------------
#this function will take command by microphone
def takecommnad():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')

        print('user said: {}\n'.format(query))
    except Exception as e:
        print("Say that again please")
        query=None
    return query

#-------------------------------------------------------------
#return only desired words to be searched
def querysorted(query):
    query=[i for i in query.split()]
    k=['wikipedia','who',"is","to",'according']
    for i in k:
        if i in query:
            query.remove(i)

    return " ".join(query)
#-----------------logic----------------------------------------
#speak("Initializing Virtual Assistant")
#wishme(MYNAME)


query=takecommnad()
query=" ".join([i.lower() for i in query.split()])




#----------------------------------------------------------
#logic for executing basic task
#Searching based on 'who' and 'wikipedia'-------------------
if ('wikipedia' in query.split()) or ('who' in query.split()):

    query=querysorted(query)
    result = wikipedia.summary(query )
    speak(result)
elif 'youtube' in query.split():


    url='youtube.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)
elif 'google' in query.split():


    url='google.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)
elif 'facebook' in query.split():


    url='facebook.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)