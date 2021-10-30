import os
import subprocess
import pyautogui
from pyscreeze import screenshot
from sphinx.util import requests
from sympy.physics.units import wb
from wikipedia import wikipedia
from Features.base_features import wishme, takeCommand, time, date, speak, open_chrome, cpu, jokes, countdown, wifi_speed
from Features.screen_record import screenrecord
from Features.wether_show import wether
from Features.sendmail import sendmail


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
                pyautogui.sleep(5)  # 5 sec to select the TAB
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

            elif "task manager" in query:
                # Ctrl+Shift+Esc: Open the Task Manager
                pyautogui.hotkey('ctrl', 'shift', 'esc')

            elif "task view" in query:
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
                print(countdown(25))  # input time 25 sec
                wifi_speed()  # calling wifi_speed function

            # <-------------------------PART-4-------------------------->

            elif "screen record" in query:
                screenrecord()

            elif"wether"in query:
                wether()

            elif "send email" in query:
                try:
                    speak("what should i say?")
                    content = takeCommand()
                    to = "receiver_email_id"  #put the id of the receiver
                    sendmail(to, content)
                    speak("Email send sucessfully")
                except Exception as e:
                    speak(e)
                    speak("unable to send the email")


    except Exception:
        print("something went wrong!")
