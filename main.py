import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from randfacts import getFact
import pyaudio #pip install pipwin , pipwin install pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1 or 0].id) which changes voice
engine.setProperty('voice', voices[0].id)

urL='https://www.google.com'
chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
#webbrowser.get('chrome').open_new_tab(urL) or .open_new or open

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("I am James Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=6)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "thank you" in query:
            speak("Happy to help you sir")   

        elif "what's your age" in query:
            speak("I'm happy to keep it as a secret") 

        elif "how are you" in query:
            speak("I'm great and you?")  

        elif "how can you help me" in query:
            speak("Well i was made for fun tasks")      

        elif 'open discord' in query:
            webbrowser.get('chrome').open_new_tab("discord.com/channels/@me")
            speak("launching Discord")

        elif 'open udemy' in query:
            webbrowser.get('chrome').open_new_tab("udemy.com")
            speak("launching udemy")

        elif 'open coursera' in query:
            webbrowser.get('chrome').open_new_tab("www.coursera.org/") 
            speak("launching coursera")   

        
        elif 'open radio' in query:
            webbrowser.get('chrome').open_new_tab("coderadio.freecodecamp.org/")
            speak("launching radio")

        elif 'open github' in query:
            webbrowser.get('chrome').open_new_tab("github.com/")
            speak("launching Github")
    
        elif 'google' in query:
            query = query.replace('in google',"")
            query = query.replace('search for',"")
            speak(f"Searching for {query} in google")
            webbrowser.open(f'https://www.google.com/search?q={query}')

        elif "search youtube" in query:
            query = takeCommand().lower()
            speak('Searching YouTube....')  
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.get('chrome').open_new_tab(url)
            speak("Search YouTube for " + str(query))

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab("youtube.com")
            speak("launching Youtube")

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab("google.com")
            speak("launching Google")


        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab("stackoverflow.com")
            speak("launching Stackowerflow") 

        elif 'open reddit' in query:
            webbrowser.get('chrome').open_new_tab("reddit.com/") 
            speak("launching reddit")   
        
        elif 'facts' in query:
            print(getFact(True)) #False to filter inappropriate facts
            speak(getFact(True))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")