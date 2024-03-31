import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening..")
            talk("Good morning sir what can i do for you")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        print("exit")
        return ""
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'whatsapp ' in command:
        pywhatkit.sendwhatmsg("+91 865 646466",
                              "fjdvjdfo sdjpjvfopv sdcjso dsfvojofdovj",
                              00, 23)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'go' in command:
        talk("no, i will not go with you")
    elif 'mad' in command:
        talk("no, i am not, you are mad")
    elif 'how' in command:
        talk("i am fine, what about u")
    else:
        talk("please say the command again")

    take_command()

run_alexa()






# import pyautogui
#
# m = pyautogui.displayMousePosition()
# print(m)
#
# import speech_recognition as sr
# import pyttsx3
# import pyautogui
#
# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
#
#
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
#
#
# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             talk("Good morning sir, what can I do for you?")
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'jarvis' in command:
#                 command = command.replace('jarvis', '')
#                 print(command)
#     except:
#         print("Exit")
#     return command
#
#
# def ask_question():
#     talk("What is the capital of France?")
#     answer = take_command()
#     return answer
#
#
# def run_alexa():
#     answer = ask_question()
#     if 'paris' in answer:
#         talk("Congratulations! You are correct!")
#         # Assuming the correct button's position is at coordinates (x, y)
#         pyautogui.click(x, y)
#     else:
#         talk("Sorry, that's incorrect. Please try again.")
#
#
# while True:
#     run_alexa()



# import speech_recognition as sr
# import pyttsx3
#
# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
#
#
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
#
#
# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             # talk("Good morning sir, what can I do for you?")
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'jarvis' in command:
#                 command = command.replace('jarvis', '')
#                 print(command)
#     except:
#         print("Exit")
#     return command
#
#
# def ask_question():
#     talk("What is the capital of France?")
#     answer = take_command()
#     return answer
#
#
# def run_alexa():
#     answer = ask_question()
#     if 'paris' in answer:
#         talk("Hooray! You are correct!")
#     else:
#         talk("Sorry, that's incorrect. Please try again.")
#
#
# while True:
#     run_alexa()