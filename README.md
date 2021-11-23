# JARVIS AI Mark - I
## Made by Gaurav Dhuria
[![IMAGE ALT TEXT HERE](https://1.bp.blogspot.com/-8-xgpYC8xQA/YM_83Y1ABZI/AAAAAAAAKow/IJhB-C8CuyAfUuN2E3jWrm6rGG1DSdxpQCLcBGAsYHQ/w660-h371/DEMO%2B%25281%2529.png)](https://youtu.be/Z5rdSA0lvNo)

####  DEMO :  [YouTube video](https://youtu.be/Z5rdSA0lvNo)

#### Discription: 
This is my JARVIS MARK-I with advance programming(ML/DL) and electronics include microcontroller and sensors My Goal was to merge AI and Electronics this was the 1st version i made Soon gonna include more advance feature in MARK II


## Built with
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>
<code><img height="30" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9bM86XXVaQme9wLJRFNk1IKtvoLEfnq22NZeP0CgHMiZc10F2ULJVoq8Ws6mlO0qpsvA&usqp=CAU"></code>
## Jarvis From Basic to Advance Tutorial
- [Part - 1](https://www.codesempai.ml/2021/10/basic-jarvis.html)
- More Parts are comming soon...
## Features

#### Demo of this project watch this [YouTube video](https://youtu.be/Z5rdSA0lvNo)

It can do a lot of cool things, some of them being:

- Greet user
- Tell current time and date
- Launch applications/softwares 
- Open any website
- Tells about weather of any city
- Open location of any place plus tells the distance between your place and queried place
- Tells your current system status (RAM Usage, battery health, CPU usage)
- Tells about your upcoming events (Google Calendar)
- Tells about any person (via Wikipedia)
- Can search anything on Google 
- Can play any song on YouTube
- Tells top headlines (via Times of India)
- Plays music
- Send email (with subject and content)
- Calculate any mathematical expression (example: Jarvis, calculate x + 135 - 234 = 345)
- Answer any generic question (via Wolframalpha)
- Take important note in notepad
- Tells a random joke
- Tells your IP address
- Can switch the window
- Can take screenshot and save it with custom filename
- Can hide all files in a folder and also make them visible again
- Has a cool Graphical User Interface
- Machine learning consept
- Deep learning consept
- face recognation
- gesture recognation

##My Coustome Features
- Costome voice
- Youtube Downloader(Auto Configuration)
- Change Wallpaper folder/Online API
- News with coustome Genre
- AI conversion Tool
- Extract Audio from Video
- Auto contrast image
- video compresser
- cricket automate
- Advance bot mode!













## ARDUINO FEATURES 
Automation and security
- Voice Opeaning and closing door 
- Turn LED on/off
- Different Light intensity
- Alert User through Motion sensor

## API Keys
To run this program you will require a bunch of API keys. Register your API key by clicking the following links

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Wolframalpha](https://www.wolframalpha.com/)
- [Google Calendar API](https://developers.google.com/calendar/auth)
  
## Installation

- First clone the repo
- Make a config.py file and include the following in it:
    ```weather_api_key = "<your_api_key>"
    email = "<your_email>"
    email_password = "<your_email_password>"
    wolframalpha_id = "<your_wolframalpha_id>"
- Copy the config.py file in Jarvis>config folder
- Make a new python environment
    If you are using anaconda just type ```conda create -n jarvis python==3.8.5 ``` in anaconda prompt
- To activate the environment ``` conda activate jarvis ```
- Navigate to the directory of your project
- Install all the requirements by just hitting ``` pip install -r requirements.txt ```
- Install PyAudio from wheel file by following instructions given [here](https://stackoverflow.com/a/55630212)
- Run the program by ``` python main.py ```
- Enjoy !!!!

## Code Structure


    ├── driver
    ├── Jarvis              # Main folder for features 
    │   ├── config          # Contains all secret API Keys
    │   ├── features        # All functionalities of JARVIS 
    │   └── utils           # GUI images
    ├── __init__.py         # Definition of feature's functions
    ├── gui.ui              # GUI file (in .ui format)
    ├── main.py             # main driver program of Jarvis
    ├── requirements.txt    # all dependencies of the program

- The code structure if pretty simple. The code is completely modularized and is highly customizable
- To add a new feature:
  -  Make a new file in features folder, write the feature's function you want to include
  - Add the function's definition to __init__.py
  - Add the voice commands through which you want to invoke the function


## Future Improvements
- Arduino interaction / Serial Comunication
- Node MCU interaction
- Generalized conversations can be made possible by incorporating Natural Language Processing
- GUI can be made more nicer to look at and functional
- More functionalities can be added
