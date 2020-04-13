import speech_recognition as sr
import pyaudio

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')

        print('user said: {}\n'.format(query))
    except Exception as e:

        query=None
    return query