import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random

warnings.filterwarnings('ignore')
#def recordaudio():

   # r = sr.Recognizer()
   # with sr.Microphone() as source:
       # print("I'm listening")
       # audio = r.listen(source)


      #  try:
            #data = r.recognize_google(audio)
           # print("you said: "+data)
      #  except sr.UnknownValueError:
            #print("I'm sorry, I did not understand that")
      #  except sr.RequestError as e:
           # print("Request results from Google Speech Recognition service error"+ e)

       # return data

def assistantResponse(text):

    print(text)

    myobj = gTTS(text= text, lang='en', slow=False)

    myobj.save('assistant_response.mp3')

    os.system('start assistant_response.mp3')

def wakeword(text):
    Wake_WORDS = ["hey mantis", "okay mantis"]
    text = text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    ordinalNumbers = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]

    result = ("today is "+weekday+" "+month_names[monthNum - 1]+" the "+ ordinalNumbers[dayNum - 1]+". ")
    print (result)
def Time():
    now = datetime.datetime.now()
    meridiem = ""
    if now.hour >= 12:
        meridiem = "PM"
        hour = now.hour - 12
    else:
        meridiem = "AM"
        hour = now.hour
    if now.minute < 10:
        minute = "0" + str(now.minute)

    result = ("it is currently " + str(hour) + ":" + minute + " " + meridiem)
    print(result)

def greeting():
#   GREETING_INPUTS = ["hi", "hey", "hello", "whats up"]
    GREETING_RESPONSE = ["hello", "howdy", "hey there"]
    result = random.choice(GREETING_RESPONSE)
    print (result)
#   for word in text.split():
#       if word.lower() in GREETING_INPUTS:
#           return random.choice(GREETINGRESPONSE)+ "."
#   return" "


print ("Hello, I am Mantis. A virtual assitant built with security in mind.")
input("how may i assist?:")
while True:
    if  ("day") in input():
        getDate()
    if ("hello") in input():
        greeting()
    if ("hello ") +("there") in input():
         print ("GENERAL KENOBI")
    if ("time") in input():
       Time()
    if ("who made you?") in input():
        print ("Aidan Bennett, a student at jackson college studying Cyber Security created me")
    if ("what can you do?") in input():
        print("I can currently give you the date, time, and execute a seperate script for packet sniffing")
    if ("sniff for arp packets") in input():
        os.system("python IDS.py")
