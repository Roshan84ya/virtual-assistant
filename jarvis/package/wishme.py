from package.speak import speak
import datetime
def wishme(MYNAME):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morining {}".format(MYNAME))
    elif hour>=12 and hour<18:
        speak("Goof AfterNoon {}".format(MYNAME))
    else:
        speak("Goof Evening {}".format(MYNAME))
    speak("Good How may i help you {} ".format(MYNAME))