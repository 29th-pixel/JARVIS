
import pyttsx3  # used in speak function
import datetime  # used to greet the user according to the time
import speech_recognition as sr  # used to listen the user through built-in microphone
import wikipedia as wiki  # used to search on wikipedia
import googlesearch  # used to search on google
import webbrowser  # open web browser on any website
import os  # os module to open different applications

def speak(audio):
    """This function make any string speak by the computer """
    print(audio)
    engine = pyttsx3.init("sapi5")
    engine.say(audio)
    engine.runAndWait()


def wishYourMaster():
    """ Function to greet the user according to the time """
    if 12 >= datetime.datetime.now().hour >= 2:
        speak("Good Morning")
    elif 12 < datetime.datetime.now().hour < 17:
        speak("Good Afternoon")
    elif 17 <= datetime.datetime.now().hour <= 24:
        speak("Good Evening ")
    speak("Sir, what can I help you for : ")


def listenUsr():
    """ this is used to detect whats the user is trying to say by converting the audio to the string that can be
    easily handled """
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("--- Listening ---")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("--- Recognising ---")
        return str(query)
    except Exception as e:
        speak(f"Not recognized with error {e}")
        return False


def usrQuery(cmnd):
    """handle given query by the user and perform the following action..."""
    if cmnd is not False:
        speak(f"Did you say {cmnd}")
        if "your name" in cmnd.lower():
            speak("My name is Jarvis and I am your virtual assistant")
        elif "what" and "time" in cmnd.lower():
            print(datetime.datetime.now())
        elif "search" in cmnd.lower():
            cmnd = cmnd.replace("search", "")
            if "wikipedia" in cmnd.lower():
                cmnd = cmnd.lower().replace("wikipedia", "")
                speak(f"According to wikipedia {wiki.summary(cmnd, sentences=3)}")
            elif "google" in cmnd.lower():
                cmnd = cmnd.lower().replace("google", "")
                for searches in googlesearch.search(query=cmnd, num=1, stop=2):
                    webbrowser.open(url=searches)
                    exit()
            elif "youtube" in cmnd.lower():
                cmnd = cmnd.lower().replace("youtube", "")
                webbrowser.open(url=f"https://www.youtube.com/results?search_query={cmnd}")
                exit()
        elif "open" in cmnd.lower():
            cmnd = cmnd.replace("open", "")
            if "youtube" in cmnd.lower():
                webbrowser.open("youtube.com")
                exit()
            elif "facebook" in cmnd.lower():
                webbrowser.open("facebook.com")
                exit()
            elif "instagram" in cmnd.lower():
                webbrowser.open("instagram.com")
                exit()
            elif "google" in cmnd.lower():
                webbrowser.open("google.com")
                exit()
            elif "geeksforgeeks" in cmnd.lower():
                webbrowser.open("geeksforgeeks.com")
                exit()
            elif "hackerrank" in cmnd.lower():
                webbrowser.open("hackerrank.com")
                exit()
            elif "visual studio code" or "vs code" or "v s code" in cmnd.lower():
                os.startfile(path="C:\\Users\\asus\\AppData\\Roaming\\Microsoft\\Windows\\Start "
                                  "Menu\\Programs\\Visual Studio Code")
            elif "pycharm" in cmnd.lower():
                os.startfile(path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains")
            elif "chrome" in cmnd.lower():
                os.startfile(path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs")
        elif cmnd.lower() == "help":
            print("it can open youtube,facebook, etc by just saying open abc \n you can search anything on wikipedia "
                  "or on google by just saying search abc on google/wikipedia/youtube \n thank u for using this "
                  "program \n please send your feedback to Mr Gurman Singh :)=")
        elif "email" in cmnd.lower():
            pass
        elif "play" in cmnd.lower():
            cmnd = cmnd.lower().replace("play", "")
            if "youtube" in cmnd.lower():
                cmnd = cmnd.lower().replace("youtube" and "on", "")
                webbrowser.open(url=f"https://www.youtube.com/results?search_query={cmnd}")
                exit()
    else:
        print("--- Try Again ---")


if __name__ == '__main__':
    wishYourMaster()
    while True:
        kya_bola = listenUsr()
        if str(kya_bola).lower() == 'stop' or str(kya_bola).lower() == 'shut up' or str(kya_bola).lower() == 'quit':
            exit()
        else:
            usrQuery(kya_bola)
    # input("Press any button to exit :)")
