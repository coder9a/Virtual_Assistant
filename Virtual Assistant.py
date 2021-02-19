import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import random
import webbrowser
import os
import smtplib

# engine object is created with API sapi5
engine = pyttsx3.init('sapi5')
# getting details of current voice
voices = engine.getProperty('voices')
'''
print(voices)
print(voices[0])
print(voices[1].id)
'''
# changing index, changes voices. 0 for male
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour <= 18:
        speak('Good afternoon Sir!')

    else:
        speak('Good Evening Sir!')

    speak('How may I help you? ')


def take_Command():
    """
    Takes microphone input from the user and returns string output
    """
    r = sr.Recognizer()  # It helps in recognizing the audio
    with sr.Microphone() as source:  # use the default microphone as the audio source
        print('Listening....')
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        # It means the system will not complete a sentence if I take break of 1 second
        audio = r.listen(source)  # listen for the first phrase and extract it into audio data

    try:  # Here, we are using try because in case some error occurs
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print('User said : ', query)

    except Exception as e:
        print(e)
        print('Say again please...')
        return 'None'
    return query


def send_Email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mymail@gmail.com', 'password')
    server.sendmail('mymail@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    greet_me()
    while True:

        query = take_Command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            # query = query.replace("wikipedia","")
            # Summary of any tittle can be obtained by using summary method
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'the time ' in query:
            steTime = datetime.datetime.now().strftime("%H:%M:%S")

        elif 'open vscode' in query:
            code_path = "C:\\Users\\Raj Balhara\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'chrome' in query:
            code_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(code_path)

        elif 'play music' in  query:
            # First we select the path of the folder where the mp3 audios are present
            path1 = 'D:\\Songs'
            # By using the listdir() method store all the files present in the folder
            files = os.listdir(path1)
            x = len(files)
            for i in files:
                print(i)
            print(x)
            n = random.randint(0,x)
            os.startfile(os.path.join(path1,files[n]))



        elif 'pycharm' in query:
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
            os.startfile(code_path)

        elif 'email' in query:
            try:
                speak('What should I write ?')
                content = take_Command()
                to = 'sender-----@gmail.com'
                send_Email(to, content)
                speak('Email sent! ')
            except Exception as e:
                print(e)
                speak('Email not sent, some failure occured ')
