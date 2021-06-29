from email import message
from email.mime import text
from typing import Text
import pyttsx3
from pywhatkit.help import sendwhatmsg
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import pywhatkit
import yagmail
import time
import pyautogui 
import requests
import os
import pyjokes
from PIL import ImageGrab
from datetime import datetime

time_now=datetime.now()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print (voices[0].id)
engine.setProperty('voice',voices[1].id)



def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    time_now=datetime.now()
    hour = int(time_now.hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon") 

    else:
        speak ("good evening")   

    speak("I am siri . Please tell me sir how can i help you?")  
          
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       
        
        print("Listnening.....")
        # r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("recognizing.....")
        query= r.recognize_google(audio, language='en-US')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please....!")
        return "None"
    return query

def sendEmail(to, subject, content):

    sender=yagmail.SMTP('samratb601@gmail.com')
    sender.send(to,subject,content)

def instant_msgTo_Whatsapp(person_name , my_msg):

    webbrowser.open('https://web.whatsapp.com/')

    time.sleep(15)
    print(pyautogui.position())

    # click on search bar
    pyautogui.click(148,153)
    pyautogui.typewrite(person_name)


    time.sleep(8)

    #click on person 
    pyautogui.click(165,271)

    time.sleep(5)

    pyautogui.typewrite(my_msg)

    time.sleep(3)
    pyautogui.press('Enter') # click on Send button

if __name__ == "__main__":
    wishMe()

    while True:
        query  =takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipidia....")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir=#select a music directory path
        #     songs= os.listdir(music_dir) 
        # #     print(songs) 
        # os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            startTime=datetime.datetime.now().strftime("%I:%M: %p")
            speak(f"sir, the time is {startTime}")
        
        elif 'open code' in query:
            codepath= r'C:\Users\SAMRAT BISWAS\AppData\Local\Programs\Microsoft VS Code\Code.exe'
            os.startfile(codepath)
        
        elif 'open word' in query:
            codepath=r'"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"'
            os.startfile(codepath)
        
        elif 'open excel' in query:
            codepath=r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(codepath)
        elif 'play' in query:
            song= query.replace('play', '')
            speak('Playing...' + song)
            pywhatkit.playonyt(song)
        elif 'joke' in query:

            print(speak(pyjokes.get_joke()))

        elif 'send mail' in query:
            
            try:
                speak("type the gmail below=>")
                reciver=str(input("Enter the gmail=>>>\n"))
                speak("what is the subject will be?")
                sbj=takeCommand().upper()
                speak("what will be the content?")
                cnt=takeCommand()
                sendEmail(to=reciver, subject=sbj ,content=cnt)
                speak("email has been sent succesfully!!")
            except Exception as e:
                print(e)
                speak("sorry my friend samrat . I am not able to send this email")

        elif 'whatsapp message' in query:
            try:
                speak("type the name below=>")
                person_name = input('Enter The Person Name Whom You Want To Send A Message: ')
                speak("what is the message will be?")
                my_msg = input('Enter Your Message: ')
                # speak("if you want to send the message imediately?")
                # query=takeCommand()
                # if 'yeah' in query:
                instant_msgTo_Whatsapp(person_name=person_name,my_msg=my_msg)
                print("Your message is sending....")
                # elif 'yes' in query:
                #     instant_msgTo_Whatsapp(person_name=person_name,my_msg=my_msg)
                #     print("Your message is sending....")
                # elif 'no' in query:
                #     speak("set the time (Hour:Miutes)")
                #     hour=int(input("enter the time in hours=>"))
                #     minutes= int(input("enter the time in minutes=>"))
                #     pywhatkit.sendwhatmsg(phone_no=mobile_number,message=whatsMsg,time_hour=hour,time_min=minutes)


            except Exception as e:
                print(e)
                speak("sorry my friend samrat . I am not able to send this whatsapp message")


