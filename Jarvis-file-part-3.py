import webbrowser
import os
import pyttsx3  # pip instll pyttx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import webbrowser as wb #pip install pycopy-webbrowser
import subprocess
import psutil  # pip install psutil
import pyautogui  # pip install pyautogui
import wikipedia  # pip install wikipedia
import pyjokes
from time import sleep
import requests
import sys #pip install os-sys
import speedtest #pip install speedtest-cli


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


def countdown(t): #defineing the function name countdown
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


if __name__ == "__main__":

 wishme()

 try:

    while True:
        query = takeCommand().lower()  # take command in queary
        print(query)

        if "time" in query:  # if time in query than assistance will say time
            time()  # function get exicuted if time in the query

        elif "date" in query:  # if date in query than assistance will say time
            date()

        elif "offline" in query:  # function to end the program
            speak("going offline")
            quit()
        # <-------------------------PART-2-------------------------->

        elif "chrome" in query:
            speak("opening the Chrome")
            open_chrome()


        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad")  # speak
            location = "C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(location)  # location of a software you want tot opem

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()  # terminate

        elif "cpu" in query:
            cpu()

        elif "screenshot" in query:
            screenshot()

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "joke" in query:
            jokes()

        elif "remember this" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember something" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())


        # <-------------------------PART-3-------------------------->

        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")

        elif "hide all files" in query or "hide this folder" in query:
            os.system("attrib +h /s /d")
            speak("Sir, all the files in this folder are now hidden")

        elif "visible" in query or "make files visible" in query:
            os.system("attrib -h /s /d")
            speak("Sir, all the files in this folder are now visible to everyone. ")

        elif "switch the window" in query or "switch window" in query:
            speak("Okay sir, select the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            sleep(5)  # 5 sec to select the TAB
            pyautogui.keyUp("alt")


        # Directly Change TAB
        # elif "switch the window" in query or "switch window" in query:
        #     speak("Okay sir, Switching the window")
        #     pyautogui.hotkey('alt','tab')
                

        elif "new virtual desktop" in query:
            # Win+Ctrl+D: Add a new virtual desktop
            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif "hidden menu" in query:
            # Win+X: Open the hidden menu
            pyautogui.hotkey('winleft', 'x')

        elif "Task Manager" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "Task view" in query:
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')

        # elif "screenshot" in query:
        #     # win+perscr
        #     pyautogui.hotkey('winleft', 'prtscr')

        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif "close this app" in query:
            # alt + f4: close this app
            pyautogui.hotkey('alt', 'f4')

        elif "setting" in query:
            # win+i = open setting
            pyautogui.hotkey('winleft', 'i')

        elif "wi-fi speed" in query:
            print(countdown(25)) #input time 25 sec
            wifi_speed() #calling wifi_speed function






 except Exception:
     print("something went wrong!")
