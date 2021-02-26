import os
from googletrans import Translator
from googletrans import LANGUAGES
import webbrowser
import time
import datetime
import speech_recognition as sr
import pyttsx3

def_name=""


translator=Translator()
r = sr.Recognizer()
mic=sr.Microphone()
engine = pyttsx3.init() 


class lang_change():
    def __init__(self,string,lan='english'):
        self.lan=lan
        self.string=string
        self.sour=self.checksour(self.string)
        self.fin=self.change(self.string,self.lan)
        
    def change(self,string,lan):
        return translator.translate(string,dest=lan).text
    def checksour(self,string):
    	return LANGUAGES[translator.translate(string).src]

class ttchange():
    def __init__(self,atext):
        self.data=atext
        self.default_name='unish' if def_name =="" else def_name
        self.rate=self.currentrate()
        self.crate=self.changerate()
        self.language=""
    def currentrate(self):
        rate=engine.getProperty("rate")
        return f'current rate is {rate}'
    def changerate(self):
        for val in self.data.split():
            if val.isnumeric():
                engine.setProperty("rate",val)
        return f'rate changed to {val}'
    def changelan(self,lan):
        self.language=lang_change.checksour(lan)
        engine.setProperty("voices",self.language)
    def changename(self):
        global def_name
        
        def_name=(self.data.split("to")[-1:])
        speak("name changed")
        return f'{def_name}'
    def changevalues(self):

        self.rate=translator.translate(self.rate,dest=self.language)
    



def speak(atext):
    engine.say(atext)
    print(atext)
    engine.runAndWait()

def reply(atext):

    ttc=ttchange(atext)
    lc=lang_change(atext)
    if 'log off' in atext or 'abort' in atext:
        speak('bye')
        speak('have a lovely day')
        exit()

    elif 'current rate' in atext:
        speak(ttc.rate)
    elif 'change rate ' in atext:
        speak(ttc.crate)
    elif 'what is your name' in atext:
        speak(f'my name is {ttc.default_name}')
    elif 'change name' in atext:
        speak(ttc.changename())
    elif 'repeat after me' in atext:
        while atext!="stop loop":
            data=take_input()
            speak(data)
    elif 'open Google' in atext :
        webbrowser.open('www.google.co.in')
    elif 'lock system' in atext:
        os.popen("gnome-screensaver-command --lock")
    

    else:
        speak("Repeat again please")

   
        

        
def take_input():
    with mic as source:
        audio = r.listen(source)
        audio_text=''
        audio_text=r.recognize_google(audio)
        return audio_text

def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if CurrentHour >= 0 and CurrentHour < 12:
        speak('Good Morning!')
    elif CurrentHour >= 12 and CurrentHour < 18:
        speak('Good Afternoon!')    
    elif CurrentHour >= 18 and CurrentHour != 0:
        speak('Good Evening!')
    speak("how may i be of assistance")
greetMe()

def unish():
    while 1:

        comand= take_input()
        reply(comand)
unish()
