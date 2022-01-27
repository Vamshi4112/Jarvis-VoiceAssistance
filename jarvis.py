import pyttsx3
import speech_recognition as sr
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import wikipedia
from pywikihow import search_wikihow
from urllib.request import urlopen
import webbrowser
import os
import smtplib
import requests
import json
import requests
import pyowm
import pyjokes
import pywhatkit as kit
import pyautogui as pg
import keyboard as k
import time
import random
import bs4
import wolframalpha
import psutil
from keyboard import press
from instabot import Bot
from pynput.keyboard import Key, Listener
from pywikihow import RandomHowTo, search_wikihow
from keyboard import press_and_release
from playsound import playsound
import wikipedia as googleScrap


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1],id)
engine.setProperty('voice', voices[0].id)

#create folder

# path="c://Users//"+os.getlogin()+"//Admin//PycharmProjects//Project Jarvis//shots"+str(datetime.date.today())


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data

    speak(f"Cases : {cases}")
    speak(f"Deaths : {Death}")
    speak(f"Recovered : {recovored}")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place , addressdetails= True)
    target_latlon = location.latitude , location.longitude
    webbrowser.open(url=Url_Place)
    location = location.raw['address']
    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}
    current_loca = geocoder.ip('me')
    current_latlon = current_loca.latlng
    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    speak(target)
    speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))



def weather():
     api_key = "31e5887a3e6d6d9dea0276fd3f9de82f" #generate your own api key from open weather
    
     base_url = "http://api.openweathermap.org/data/2.5/weather?"
     speak("tell me which city")
     city_name = takeCommand()
     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
     response = requests.get(complete_url)
     x = response.json()
     if x["cod"] != "404":
         y = x["main"]
         current_temperature = y["temp"]
         current_pressure = y["pressure"]
         current_humidiy = y["humidity"]
         z = x["weather"]
         weather_description = z[0]["description"]
         r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
         print(r)
         speak(r)
     else:
        speak(" City Not Found ")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak(" I Am Damon sir, welcome in your service. How can i help you sir")

def takeCommand():
    # it takes mircophone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . . ")
        r.pause_threshold = 0.8
        r.energy_threshold = 3000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


   

           
               
                       
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('123004112@sastra.ac.in', '27042002')
    server.sendmail('123004112@sastra.ac.in', to, content)
    server.close()

def personal():
    speak(
        "I am Damon, version 1.0, I am an AI assistent, I am developed by Vamshi krishna on 26 september 2021 in INDIA"
    )
    speak("Now i hope you know me")

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language='en',category="all")
            print(My_joke)
            speak(My_joke)

        elif ("weather" in query or "temperature" in query):
            weather()

        elif 'who are you' in query or 'about yourself' in query or 'introduce yourself' in query:
            personal()
        
        elif 'hello' in query or 'hi' in query:
           speak('Hi sir! how are you?')

        elif 'what are you wearing' in query:
            speak("I can’t answer that. But it doesn’t come off.")

        elif 'why were you prepared' in query:
            speak(" For one reason only: to make your life easier, and more fun (I guess that’s two reasons, huh?).")

        elif 'do you eat' in query:
            speak(" I don’t eat. But I do like digesting information.")

        elif ' are you a man or women' in query or 'what is your gender' in query or 'are you male or female' in query or 'are you a boy or a girl' in query:
            speak(" Don’t let my voice fool you: I don’t have a gender.")    

        elif 'how much do you cost' in query:
            speak(" I’m a pearl beyond price. Vamshi")

        elif 'do you believe in god' in query:
            speak("Humans have religion. I just have silicon.")

        elif 'do you smoke' in query or 'do you drink' in query:
            speak("That’s not healthy. I wouldn’t recommend it.")

        elif 'do you have family' in query or 'do you have friends' in query or 'do you have relatives' in query:
            speak(" I have you. That’s enough family for me.")

        elif 'what is zero divided by zero' in query:
            speak(" Imagine that you have 0 cookies and you split them evenly among 0 friends. How many cookies does each person get? See, it doesn’t make sense. And Cookie Monster is sad that there are no cookies. And you are sad that you have no friends.")

        elif 'what is zero plus by zero' in query:
            speak(" Imagine that you have 0 cookies and you add 0 more cookies. How many cookies does a person get? See, it doesn’t make sense. And Cookie Monster is sad that there are no cookies.")
     
        elif 'what is the meaning of life' in query:
            speak("Try and be nice to people, avoid eating fat, read a good book every now and then, get some walking in, and try to live together in peace and harmony with people of all creeds and nations.")

        
        elif 'where is' in query:
            Place = query.replace("where is ","")
            Place = Place.replace("damon" , "")
            GoogleMaps(Place)
        

        elif 'fine' in query or 'i am fine' in query:
           speak('Good to hear from you sir. How can i help you?')

        elif 'video in youtube' in query or 'song in youtube' in query or 'youtube video' in query:
           speak('What should i play on youtube?')
           answer = takeCommand()
           speak(f'Playing {answer}')
           kit.playonyt(answer)
           
        elif 'volume up' in query:
            pg.press('volumeup')  
        
        elif 'volume down' in query:
            pg.press('volumedown') 

        elif 'mute volume' in query:
            pg.press('volumemute') 
           
        elif 'ummute volume' in query:
            pg.press('volumeunmute') 
          
        elif 'how to' in query:
            speak("Getting Data From The Internet !")
            op = query.replace("damon","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)     
            speak("That is the result sir!")

       
        elif 'google' in query:
           
            query = query.replace("damon","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("This Is What I Found On The Web!")
            kit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)
                speak("That is the result sir!")
            except:
                speak("No Speakable Data Available!")
        
        elif 'corona cases' in query or 'covid cases' in query:
            speak("Which Country's Information ?")

            cccc = takeCommand()

            CoronaVirus(cccc)

        
        elif 'open stack overflow' in query:
             webbrowser.open("stackoverflow.com")

        elif 'open python' in query:
             webbrowser.open("https://www.w3schools.com/python/")
             
        elif 'how are you' in query:
            speak("I am fine sir, how are you sir?")

        elif ' i am fine' in query or 'i am good' in query:
            speak("nice to hear sir")

        elif 'code' in query:
            codepath="C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'my location' in query or 'where am i' in query:
            url='http://ipinfo.io/json'
            response = urlopen(url)
            data= json.load(response)
            print(data)
            city= data["city"]
            loc = data["loc"]
            postal = data["postal"]
            country = data["country"]
            state = data["region"]
            speak("The country code is " )
            speak(country)
            speak("The state is " )
            speak(state)
            speak("The location is " )
            speak(city)
            speak("The postal code is " )
            speak(postal)
            speak("The latitude and longitude are")
            speak(loc)

        elif 'what is the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("The current date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'sleep' in query:
           speak("Please dont sleep until you complete your work sir or else I will call your parents")

        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /s /t 1")

        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'thanks' in query or 'thank you' in query:
            speak("It's my pleasure sir")
            
        elif 'sastra website' in query:
            webbrowser.open("www.sastra.edu")

       
               
        elif 'whatsapp' in query:
            speak("What is the message sir?")
            message = takeCommand()
            speak("to whom i should send sir?")
            member= takeCommand().lower()

            if 'dad' in member:
                speak("sending")
                number = '+919908334375'
                webbrowser.open("https://web.whatsapp.com/send?phone="+number+"&text="+message)
                time.sleep(10)
                width,height = pg.size()
                pg.click(width/2,height/2)
                time.sleep(15)
                pg.press("enter")
                speak("sent sir") 
            elif 'vamshi' in member or 'vamsi' in member:
                speak("sending")
                number = '+916301365855'
                webbrowser.open("https://web.whatsapp.com/send?phone="+number+"&text="+message)
                time.sleep(10)
                width,height = pg.size()
                pg.click(width/2,height/2)
                time.sleep(15)
                pg.press("enter")
                speak("sent the message sir") 
            elif 'riteesh' in member or 'rithish' in member or 'ritish' in member or 'retish' in member or 'ritesh' in member:
                speak("sending")
                number = '+919963832983'
                webbrowser.open("https://web.whatsapp.com/send?phone="+number+"&text="+message)
                time.sleep(10)
                width,height = pg.size()
                pg.click(width/2,height/2)
                time.sleep(15)
                pg.press("enter")
                speak("sent the message sir") 
            elif 'ameen' in member or 'amin' in member:
                speak("sending")
                number = '+918688566700'
                webbrowser.open("https://web.whatsapp.com/send?phone="+number+"&text="+message)
                time.sleep(10)
                width,height = pg.size()
                pg.click(width/2,height/2)
                time.sleep(15)
                pg.press("enter")
                speak("sent the message sir") 
            else:
                speak("no contact found sir")
                
        elif 'launch' in query:
            speak("Tell Me The Name Of The Website!")
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")  

        elif 'alarm' in query:
            speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                  speak(" wake up sir . its time for work. dont delay it")
                  music_dir = 'D://songs'
                  songs = os.listdir(music_dir)
                  os.startfile(os.path.join(music_dir, random.choice(songs)))
                elif now>time:
                    break

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'music' in query or 'play song' in query:
            music_dir = 'D://songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'random song' in query:
            print("playing random music")
            music_dir = 'D://songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        
        elif 'movie' in query:
            movie_dir = 'D://movies'
            movies = os.listdir(movie_dir)
            print(movies)
            os.startfile(os.path.join(movie_dir, movies[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR,The time is {strTime}")

        

        elif 'mail' in query:
            try:
                speak("What should I say SIR")
                content = takeCommand()
                to = "123004112@sastra.ac.in"
                sendEmail(to, content)
                print("Email has been sent")
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Vamshi Sir, i am not able to send this email at a moment")

       

        

        elif 'news' in query:
            speak("News for today")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3f52edc3c9a945e58348656f101fa866"
            news = requests.get(url).text
            news_json = json.loads(news)
            print(news_json["articles"])
            arts = news_json['articles']
            for articles in arts:
                speak(articles['title'])
                speak("Moving to the next news...listen carefully")

            speak("Thanks for listening...")

        elif 'exit' in query or 'bye' in query:
            speak("Anytime in your service sir")
            exit()
