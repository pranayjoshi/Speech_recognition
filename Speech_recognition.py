"""Project name = Pranay Assistant(pj assist)
    Name = pj assist
    Developer Name = Pranay Joshi
    Version = 1.0
    Old modules = Speech recognition, GTTs, PyAudio, os, re, webbrowser, smtplib, certifi, requests, pyttsx3 etc.
    """
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import pyttsx3
engine = pyttsx3.init()
engine.say("hi user")
engine.runAndWait()
def speak(text):

    engine.say(text)
    engine.runAndWait()

speak('before asking command you have to call me PJ assist first. For example')
speak('pj assist open developer\'s website')
speak('this will open sir pranay\'s website')
speak('some of its command are as follows: shutdown, open reddit with any form, open facebook, open amazon, gives wether report,'
                'gives city reports, tell some jokes, and other then this it can search not matched words with google')



def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:

        speak('i am ready for your command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        speak('you said:' + command +'\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        speak("Your last command couldn\'t be heard")
        command = myCommand();

    return command

def assistant(command):
    "if statements for executing commands"

    if 'pj assist open reddit' in command:
        con = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if con:
            subreddit = con.group(1)
            url = url + 'r/' + subreddit
            webbrowser.open(url)
            speak("done")
    if 'pj assist open youtube' in command:
        url = 'https://www.youtube.com/'
        webbrowser.open(url)
        speak('done')
    elif 'what\'s your actual name' in command:
        speak("Pranay\'s Assistant")

    elif 'pj assist open website' in command:
        con = re.search('open website (.+)', command)
        if con:
            domain = con.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak('done')
    elif 'pj assist open facebook' in command:
        url = 'https://www.facebook.com/'
        webbrowser.open(url)
        speak('done')
    elif 'pj assist open amazon' in command:
        url = 'https://amazon.in/'
        webbrowser.open(url)
        speak('done')
    elif 'pj assist open developers website' in command:
        url = 'https://pranayteaches.wixsite.com/pranayteaches'
        webbrowser.open(url)
        speak('done')
    elif 'pj assist open developers github' in command:
        url = 'https://github.com/pranayteaches/'
        webbrowser.open(url)
        speak('done')
    elif 'what\'s up' in command:
        engine = pyttsx3.init()
        engine.say('Just doing my thing')
    elif 'pj assist tell some joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
        else:
            speak('oops!I ran out of jokes')

    elif 'pj assist what\'s current weather in' in command:
        con = re.search('current weather in (.*)', command)
        if con:
            city = con.group(1)
            url2 = 'https://api.openweathermap.org/data/2.5/weather?appid=608e56270a3d78b4012bbfdda0f05234&q=' + city
            res = requests.get(url2)
            database = res.json()
            temp = database['main']['temp']
            wind = database['wind']['speed']
            overall = database['weather'][0]['main']
            speak(f'The Current weather in  is {overall}. The tempeture is {temp}.1f degree. it\'s wind speed is {wind} ')

    elif 'find longitude and latitude of' in command:
        con = re.search('find longitude and latitude of(.*)', command)
        if con:
            city = con.group(1)
            url2 = 'https://api.openweathermap.org/data/2.5/weather?appid=608e56270a3d78b4012bbfdda0f05234&q=' + city
            res = requests.get(url2)
            database = res.json()
            lat = database['coord']['lat']
            long = database['coord']['lon']
            speak(f'it\'s latitude is {lat}. it\'s longitude is {long}.')

    elif 'pj assist open photoescape' in command:
        loca = '"C:\Program Files (x86)\PhotoScape\PhotoScape.exe"'
        os.system(loca)
        speak('done')
    elif 'pj assist open filmora' in command:
        loca = '"C:\Program Files\Wondershare\Filmora\Filmora.exe"'
        os.system(loca)
        speak('done')
    elif 'pj assist open pycharm' in command:
        loca = 'C:\Program Files\JetBrains\PyCharm Community Edition 2018.3.2\bin\pycharm64.exe'
        os.system(loca)
        speak('done')
    elif 'pj assist open bandicam' in command:
        loca = "D:\Bandicam"
        os.system(loca)
        speak('done')
    elif 'pj assist open email' in command:
        speak("'Who is the recipient?'")

        recipient = myCommand()

        if 'anyone' in recipient:
            speak('What should I say?')
            content = myCommand()

            # init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', )

            # identify to server
            mail.ehlo()

                # encrypt session
            mail.starttls()

                # login
            mail.login('pranayjoshi446677@gmail.com', 'narayan446677')

                # send message
            mail.sendmail('Pranay Joshi', 'pranayjoshi4466@gmail.com', content)

                # end mail connection
            mail.close()

            speak('Email sent.')

    elif 'pj assist shutdown' in command:

        speak('understood sir')

        speak('connecting to command prompt')

        speak('shutting down your computer')

        os.system('shutdown -s')

    elif'pj assist quit' in command:

        speak('ok sir')

        speak('closing all systems')

        speak('disconnecting to servers')

        speak('going offline')

        quit()
    else:
        searcher = 'https://www.gooogle.co.in/search?q=' + command
        webbrowser.open(searcher)
        speak('done')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
