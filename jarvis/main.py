
from package.speak import speak
from package.querysorted import querysorted
from package.takecommand import takecommand
from package.wishme import wishme
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import smtplib

MYNAME='Roshan'

speak("Initializing Virtual Assistant")
wishme(MYNAME)





query=takecommand()
while query==None:

    speak("You have not said anything ")
    speak("Do you want a break")
    query = takecommand()
    if query==None:
        continue

    elif query.lower()=='yes':
        speak('okay Have a nice day {}'.format(MYNAME))
        exit()
    else:
        break

query=" ".join([i.lower() for i in query.split()])




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
elif 'play' in query.split() and 'music' in query.split():
    songs_dir = "C:\\Users\\Roshan84ya\\Music"
    songs = os.listdir(songs_dir)

    os.startfile(os.path.join(songs_dir ,songs[0]))
elif ('the time' in query) or ('time' in query):
    strtime=datetime.datetime.now().strftime("%H:%M:%S")
    speak("It's {}".format(strtime))
elif 'say' in query.split() or 1:

    
    speak(query)