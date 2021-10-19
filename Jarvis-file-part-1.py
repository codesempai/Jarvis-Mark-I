import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 170
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 2:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("how can i help u?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please..")

        return "None"
    return query


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()  # take command in queary
        print(query)

        if "time" in query:  # if time in query than assistance will say time
            time()           #function get exicuted if time in the query
        elif "date" in query:  # if date in query than assistance will say time
            date()
        elif "offline" in query:  # quit to end the program
            speak("going offline")
            quit()
