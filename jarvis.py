from tkinter.constants import COMMAND
import speech_recognition as sr
import smtplib
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from email.message import EmailMessage
import requests
import time
import math
import os 
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import ttk
from tkinter import *
import  json
import cv2

from playsound import playsound
import PIL.Image
import sys, os
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
   engine.say(text)
   engine.runAndWait()
def take_command():
   try:
       with sr.Microphone() as source:
           print("computing......................")
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command = command.lower()
           if 'sars' in command:
               command = command.replace('sars', '')
               print(command)
   except:
       pass
   return command
def speak(float):
   engine.say(float)
   engine.runAndWait()
def take_query():
   try:
       with sr.Microphone() as source:
           print("computing......................")
           sound = listener.listen(source)
           query = listener.recognize_google(sound)
   except:
       pass
   return query


 
        
        
def api():
    api_key = "560da8aa46d3ec09a781846c66798a10"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    talk('please say me your city name')
    city_name = take_command()
    print(city_name)
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    if response.status_code == 200:

        data = response.json()
        main = data['main']
        temperature = main['temp']
        temp_feel_like = main['feels_like'] 
        humidity = main['humidity']
        pressure = main['pressure']
        weather_report = data['weather']
        wind_report = data['wind']
        talk('the weather is')
        talk(temperature)
        talk(temp_feel_like)
        talk(humidity)
        talk(pressure)
        talk(weather_report)
        talk(wind_report)
    else:
        talk('http error')
   
# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    # attempt to open image from user-input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
     # Make sure to give app access in your Google account
    server.login('smritishakyo2012@gmail.com', 'dadu1948@123#$')
    email = EmailMessage()
    email['From'] = 'smritishakyo2012@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
email_list = {
    'mother': 'moumita.deb.choudhury@gmail.com',
}
def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('done boss')
def pynewsindia():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=2f0834cfb909401a9cca0ce40cd389f2"
    open_google_page = requests.get(main_url).json()
    articles = open_google_page["articles"]

    result = []

    for a in articles:
        result.append(a["title"])

    for i in range(10):
        time.sleep(5)
        Headline = i+1, result[i]
        print(Headline)
        talk(Headline)

#defprintSomething():
    #print (get_info())

#root = Tk()

#button = Button(root, text="Print Me", command=printSomething)
#button.pack()
def alarm():

    alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
    alarm_hour=alarm_time[0:2]
    alarm_minute=alarm_time[3:5]
    alarm_seconds=alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()
    print("Setting up alarm..")
    
    while True:
        now = datetime.datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")
        if(alarm_period==current_period):
            if(alarm_hour==current_hour):
                if(alarm_minute==current_minute):
                    if(alarm_seconds==current_seconds):
                        print("Wake Up!")
                        talk("wake up bro you have to go to school wake up wake up wake up wake up")
                        break

def shakyo():
   command = take_command()
   print(command)
   if 'play' in command:
       song = command.replace('play', '')
       talk('ok i will play it for you' + song)
       pywhatkit.playonyt(song)
   
   elif 'what is my favorite language' in command:
       talk('python is my favorite language')
   elif 'time' in command:
       time = datetime.datetime.now().strftime('%I:%M %p')
       talk('Bro the time is' + time)
   elif 'google' in command:
       son = command.replace('google', '')
       talk('ok i will play it for you' + son)
       ini=pywhatkit.info(son, lines=3)
       print(ini)
       talk("happy reading")
       


   elif 'say me about' in command:
       person = command.replace('say me about', '')
       info = wikipedia.summary(person, 10)
       print(info)
       talk(info)
   elif 'close the porgramme' or 'stop' or'thank you' in command:
       talk("thank you for using shakyo's ai")
       os.close("jarvis.py", os.O_RDWR|os.O_CREAT )
   elif 'open meet' in command:
       talk('yes bro i will open it for you')
       webbrowser.open('https://meet.google.com/?authuser=1')
   elif 'open youtube' in command:
        talk('yes bro i will open youtube')
        webbrowser.open("https://www.youtube.com/?authuser=1") 
   elif 'who am i' in command:
       talk('you are my master because you have made me using python and hours of hardwork')
   elif 'who are you' in command:
       talk('i am sars an ai made by you, please say me how can i help you ')
   elif 'joke' in command:                                
       talk(pyjokes.get_joke())
   elif 'open classroom' in command:
       talk('ok bro i will open it for you')
       webbrowser.open('https://classroom.google.com')
   elif 'open spotify' in command:
       talk ('I will open it for you')
       webbrowser.open("https://g.co/kgs/wb4KQQ")
   elif 'open google' in command:
       talk('ok man i will open it for you')
       webbrowser.open('https://www.google.com/?authuser=1')
   elif 'open my messages' in command:
       talk('ok i will open hangouts for you')
       webbrowser.open('https://hangouts.google.com/?authuser=1')
   elif 'repeat after me' in command:
       talk('ok bro i will repeat after you')
       das=get_info()
       talk(das)
   elif 'take a screenshot' in command:
       pywhatkit.take_screenshot
   elif 'who are my best friends' in command:
       talk('you do not have any best friends because all are useless in this world and you are too expensive to others')
   elif 'covid hostipals near me' in command:
       talk('ok bro i have found a hospital near you')
       webbrowser.open('https://g.page/RMHofficial?share')
   elif 'send a whatsapp message' in command:
       talk('ok i will send the message but please type the message')
       phno=str(input('enter the reciver phone number : '))
       talk('please say you message')
       msg= get_info()
       talk('ok done')
       hour=int(input('enter in which hour you want to send the message(12hrclock): '))
       minu=int(input('enter in which minute  you want to send the message: '))
       pywhatkit.sendwhatmsg(phno, msg,hour, minu )

   elif 'who is prathamesh' in command:
       talk('prathamesh is a jerk who does not know how to speak and acts as if he is the victim 24/7 total jerk, that guy does not even know how to talk to techers. prathamesh is nothing but a bitch lasagna')
   elif 'how to make pizza' in command:
       talk('ok i will tell you how to make a pizza. you have to just watch the video which i will show you now')
       webbrowser.open('https://youtu.be/BFJ9Fjqa2-k')
   elif 'how to be sad' in command:
       talk('be like shakyo to be sad')
   elif 'the weather in ' in command:
       info1 = pywhatkit.search(command)
       tin=str(info1)
       dash=print('the weather is'+tin) 
       talk(dash)      
   elif 'who is the worst person on earth' in command:
       talk('shakyo is the worst person on earth, we all hate him and we will kill him he has no right to be alive ')
   elif 'heron formula' in command:
    talk('please give the sides of the triangle in the below form')
    sh1=float(input('enter the first side of the triangle : '))
    sh2=float(input('enter the second side of the triangle : '))
    sh3=float(input('enter the third side of the triangle : '))
    sh4=sh1 + sh2 + sh3
    sh5=sh4/2
    sh6=sh5-sh1
    sh7=sh5-sh2
    sh8= sh5-sh3
    sh9= sh5*sh6*sh7*sh8
    sh10= sh9**0.5
    print('the answer is :', sh10)
    talk(sh10)
   elif 'search ' in command:
       bakwas = command.replace('search', '')
       talk('ok i will search it for you' + bakwas)
       pywhatkit.search(bakwas)
   elif 'repeat after me ' in command:
       talk(command)
   elif 'open google chrome' in command:
       talk('ok i will open it for you')
   elif 'send a mail' in command:
       talk('ok i will send the mail for you')  
       h = 1
       while h < 2:
           get_email_info()
       h = h+1
   elif 'answer the following' in command:
       talk('ok i will search the answer the answer for you in google')
       pywhatkit.search(command)
   elif 'modify this image' in command:
       talk('ok i will do it for you')
       w=1
       while w>2:
           main()
           w=w+1
   elif 'weather' in command:
       g=1
       while g<2:
           api()
       g=g+1
   elif 'news' in command:
       talk('ok i will tell the news for you')
       k=1
       while k<2:
           pynewsindia()
       k=k+1
   elif 'my calculator' in command:
       talk('ok')
       os.startfile("templates\dash.py")
   elif 'set timer' or 'wake me up' or'set alarm' in command:
       talk('ok but you have enter the time below')
       dk=0
       while dk<1:
            alarm()
            dk=dk+1 
         
   else:
       talk('the command which you gave is out of my code list kindly assign me something else.')
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good morning I am sars Sir. Please tell me how may I help you")
    elif hour>=12 and hour<18:
        talk("Good Afternoon! I am sars  Sir. Please tell me how may I help you")   
    else:
        talk("Good Evening! I am sars Sir. Please tell me how may I help you")  
i = 1
while i < 2:
  wishme()
  i = i+1
while True:
   shakyo()
 
