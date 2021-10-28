import webbrowser
import pyttsx3  # pip instll pyttx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import psutil  # pip install psutil
import pyautogui  # pip install pyautogui
import pyjokes
from time import sleep
import sys  # pip install os-sys
import speedtest  # pip install speedtest-cli


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
        print("Say that again please..")

        return "None"
    return query


def cpu():
    usage = str(psutil.cpu_percent())  # cpu percentage
    print(usage)
    speak("cpu is at" + usage + "percentage")

    battery = psutil.sensors_battery()  # battery percentage
    print(battery.percent)
    speak("battery is at")
    speak(battery.percent)
    speak("percentage")

    speak("used R A M and available memory is printed")

    # you can have the percentage of used RAM
    virtual_memory = psutil.virtual_memory()
    print(virtual_memory.percent)

    # you can calculate percentage of available memory
    available_memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    print(available_memory)


def open_chrome():
    # url u want to open
    url = 'http://docs.python.org/'

    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # replace chrome_path with the correct path for your platform.

    # MacOS
    # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)
    # call the function


def screenshot():
    img = pyautogui.screenshot()
    img.save("D:/screenshot_1.png")  # file mane and location
    speak("Done")


def jokes():
    speak(pyjokes.get_jokes())


def countdown(t):  # defineing the function name countdown
    while t > 0:
        sys.stdout.write('\rProcessing time : {}s'.format(t))
        t -= 1
        sys.stdout.flush()
        sleep(1)


def wifi_speed():
    s = speedtest.Speedtest()

    print('My download speed is:', s.download())
    print('My upload speed is:', s.upload())

    best_server = s.get_best_server()
    for key, value in best_server.items():
        print(key, ' : ', value)


