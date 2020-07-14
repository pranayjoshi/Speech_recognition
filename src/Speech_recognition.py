"""
    Project name = Pranay Assistant(Indo)
    Name = Indo
    Developer Name = Pranay Joshi
    Version = 2.0
    Old modules = Speech recognition, GTTs, PyAudio, os, re, webbrowser, smtplib, certifi, requests, pyttsx3 etc.
    New Modules = google, word2number, wikipedia, time, json, datetime, ctime
"""

import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import pyttsx3
import time
from time import ctime
from word2number import w2n as converse
import wikipedia
import json
from datetime import date

# Defining global variables

engine = pyttsx3.init()         # defining pyttsx3
indo = ["indo", "endo"]         # deining the name by which the assistant will be called

# Intial defines
def speak(text):        # This speak command will speak the text
    engine.say(text)
    engine.runAndWait()
speak("Hi Pranay")          # Checking by speaking the developers name

def today():        # defining this to get the date
    today = date.today()
    return today

def present(l, command):        # funtion used to check if the command is called by the user or not
    ls = []
    for i in indo:
        for j in l:
            get = str(i)+ " " + str(j)
            if get in command:
                return True
                break

# Important function for recogninzing voice
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

# This is the main assistant
def assistant(command):
    # Deining important variables and calling some files
    with open("mailing_list.json", "r+") as file:       #for mailing system
        data1 = json.load(file)
    mailing_list = data1
    recipient_name = list(data1.keys())
    
    with open("app_file.json", "r+") as file:       # For opening apps
        data2 = json.load(file)
    location = data2
    apps = list(data2.keys())
    with open("app_file.json", "r+") as file:       # For opening apps
        data3 = json.load(file)
    link= data3
    web = list(link.keys())
    # fun questions
    if 'hey indo what\'s your actual name' in command:
        speak("Pranay\'s Assistant")
    elif present(['what\'s up'],command):
        speak('Just doing my thing')

    # Web based statements
    elif present([(f"open {i}") for i in web], command):    # websites in websites.json
        con = re.search('open (.*)', command)
        con = con.group(1)
        url = link[con]
        webbrowser.open(url)
        speak('done')
    elif present(['open website'], command):        # websites in realtime
        con = re.search('open website (.+)', command)
        if con:
            domain = con.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak('done')
    # web based commands/scrapping

    # jokes
    elif present(['tell some jokes', 'tell some joke', "tell me some jokes", "tell me some joke"], command):
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
        else:
            speak('oops!I ran out of jokes')

    # Wikipedia Search
    elif present(["wikipedia search", "search in wikipedia"], command):
        con = re.search('for (.*)', command)
        con = con.group(1)
        speak(f"What do you want to hear about {con} , It's Definition, A short summary, A summary, or view full page content")
        response = myCommand();
        if "definition" in response:
            speak(f"here is the defination of {con}, " + wikipedia.summary(con, sentences=2))
        elif "short summary" in command:
            speak(f"here is a short summary of {con}," + wikipedia.summary(con, sentences=4))
        elif " summary" in command:
            speak(f"here is a quick summary of {con}" + wikipedia.summary(con))
        elif "page content" in command:
            print(f"here is the full page content of {con}" + wikipedia.page(con).content)
        else:
            print("invalid command!")

    # Whether

    elif present(['what\'s current weather in'],command):
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
   
    # Longitude & Latitude
    elif present(['find longitude and latitude of'],command):
        con = re.search('find longitude and latitude of(.*)', command)
        if con:
            city = con.group(1)
            url2 = 'https://api.openweathermap.org/data/2.5/weather?appid=608e56270a3d78b4012bbfdda0f05234&q=' + city
            res = requests.get(url2)
            database = res.json()
            lat = database['coord']['lat']
            long = database['coord']['lon']
            speak(f'it\'s latitude is {lat}. it\'s longitude is {long}.')
   
    # opens apps
    elif present([(f"open {i}") for i in apps],command):
        con = re.search('open (.*)', command)
        con = con.group(1)
        val = location[con]
        os.startfile(val)
        speak('done')

    # Sending email
    elif present(['open email', "send mail"], command):
        speak("'Who is the recipient?'")

        recipient = myCommand()

        if recipient in recipient_name:
            speak('What should I say?')
            content = myCommand()

            # init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', )

            # identify to server
            mail.ehlo()

                # encrypt session
            mail.starttls()

                # login
            mail.login('yourname@gmail.com', 'pass123')

                # send message
            mail.sendmail(recipient, mailing_list[recipient], content)

                # end mail connection
            mail.close()

            speak('Email sent.')
    # OS based commands
    # Computer shutdown
    elif 'indo shutdown' in command:

        speak('understood sir')

        speak('connecting to command prompt')

        speak('shutting down your computer')

        os.system('shutdown -s')

    # stope compiling
    elif 'indo quit' in command:

        speak('ok sir')

        speak('closing all systems')

        speak('disconnecting to servers')

        speak('going offline')

        quit()

    #present time
    elif "indo what's the time" in command:
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        speak(time)

    # present date
    elif present(["what's the date", "what is the date today", "what is the date", "today's date","what is today's date"],command):
        d2 = today().strftime("%B %d, %Y")
        speak(f"today's date is{d2}")

    # pausing the script
    elif present(["pause for", "wait for"], command):
            con = re.search('for (.*)', command)
            con = str(con.group(1))
            l = con.split()
            con = l[0]
            con = int(con)
            con_st = l[1]
            print(con)
            con = int(con)
            check = "seconds"
            minute = ["minutes", "mins", "minute"]
            if con_st in minute:
                con *= 60
                check = "minutes"
            speak(f"Okay! I am taking rest for {con} {check}")
            time.sleep(con)
    # google based search commands

    # Google search results
    elif present(['show the results for', "google search", "google", "results of"],command):
        con = re.search('results for (.*)', command)
        con = con.group(1)
        try: 
            from googlesearch import search 
        except ImportError:  
            print("No module named 'google' found") 
        l = []
        query = command
        i = 1
        for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
            print(str(i) + "\t" + j) 
            l.append(j)
            i += 1
        speak("Which website do you want to see. Speak the number")
        res = myCommand();
        print("okay")
        final = converse.word_to_num(res)
        webbrowser.open_new_tab(l[final])

    # Search for results in youtube
    elif present(["open youtube", "open youtube and search for", "youtube search", "youtube"],command):
        con = command.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + con
        webbrowser.get().open(url)
        speak("Here is what I found for " + con + "on youtube")
    # rest search in google    api = btnG=1&q=
      
    else:
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=' + command)

#loop to continue executing multiple commands
while True:
    assistant(myCommand())