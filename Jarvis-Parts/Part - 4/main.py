import os
import subprocess
from time import sleep
import pyautogui
from pyjokes import pyjokes
from sympy.physics.units import wb
from wikipedia import wikipedia
from default.AI_assistant.FEATURES.basic import takeCommand, time, date, open_chrome, speak
def play_songs():
    pass


if __name__ == "__main__":

    # wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        if "date" in query:
            date()

        # Open chrome/Website
        if "open chrome" in query:
            open_chrome()

        # Wikipedia search
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            print(result)

        # Chrome search
        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")


        # Launch applications
        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad")  # speak
            location = "C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(location)  # location of a software you want tot opem

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()  # terminate


        # Random jokes
        elif "joke" in query:
            speak(pyjokes.get_jokes())

        # Logout / Shutdown / Restart
        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('initiating restart in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")

            # <-------------------------Pyautogui  Features--------------------->

        elif "hidden menu" in query:
            # Win+X: Open the hidden menu
            pyautogui.hotkey('winleft', 'x')

        elif "task manager" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "task view" in query:
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')

        elif "take screenshot" in query:
            # win+perscr
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")

            # Take screenshot save in Given location
            '''        
        elif "take screenshot" in query:
            img = pyautogui.screenshot()
            img.save("D:/screenshot_1.png")  # file mane and location
            speak("Done")
            '''

        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif "close the app" in query:
            pyautogui.hotkey('alt', 'f4')

        elif "new virtual desktop" in query:
            # Win+ctrl+d : add new virtual desktop
            pyautogui.hotkey('winleft', 'ctrl', 'd')


        elif "play songs" in query:
            play_songs()
