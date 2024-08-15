import datetime
import os
import speech_recognition as sr
import pyttsx3
import openai
import webbrowser

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-usa")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry!"


if __name__ == '__main__':

    say("Hy Waleed, How can I help you")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: add more sites to access easily
        sites = [['google', 'https://www.google.com'], ['youtube', 'https://www.youtube.com'],
                 ['gmail', 'https://www.gmail.com'], ['facebook', 'https://www.facebook.com'],
                 ['Linkedin', 'https://www.linkedin.com'], ["Whatsapp","https://web.whatsapp.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} ...")
                webbrowser.open(site[1])

        # todo: feature for playing a specific music
        musicpath = r"E:\Songs\KIRA-NewWorld.mp3"
        if "open music" in query:
            os.system(f"start {musicpath}")
            say("Opening music...")

        # For datetime
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            say(f"The time is {strfTime}")

        # For open app
        if "open camera" in query.lower():
            os.system("start microsoft.windows.camera:")
            say("Opening camera...")


# # =============================================================
# todo: this below code work when you have working openai api key with tokens
# # =============================================================
# import os
# import webbrowser
# import openai
# import datetime
# import random
# import numpy as np
# import speech_recognition as sr
# import pyttsx3
# from config import apikey
#
# engine = pyttsx3.init()
#
# chatStr = ""
#
# def chat(query):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"Waleed: {query}\n Jarvis: "
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     say(response["choices"][0]["text"])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return response["choices"][0]["text"]
#
# def ai(prompt):
#     openai.api_key = apikey
#     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
#
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=200,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     text += response["choices"][0]["text"]
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")
#
#     with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
#         f.write(text)
#
# def say(text):
#     engine.say(text)
#     engine.runAndWait()
#
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language="en-usa")
#             print(f"User said: {query}")
#             return query
#         except Exception as e:
#             return "Some Error Occurred. Sorry from Jarvis"
#
# if __name__ == '__main__':
#     print('Welcome to Jarvis A.I')
#     say("Jarvis A.I")
#     while True:
#         print("Listening...")
#         query = takeCommand()
#         sites = [['google', 'https://www.google.com'], ['youtube', 'https://www.youtube.com'],
#                  ['gmail', 'https://www.gmail.com'], ['facebook', 'https://www.facebook.com'],
#                  ['Linkedin', 'https://www.linkedin.com'], ["Whatsapp","https://web.whatsapp.com"]]
#
#         for site in sites:
#             if f"Open {site[0]}".lower() in query.lower():
#                 say(f"Opening {site[0]} sir...")
#                 webbrowser.open(site[1])
#
#             musicpath = r"E:\Songs\KIRA-NewWorld.mp3"
#             if "open music" in query:
#                 os.system(f"start {musicpath}")
#                 say("Opening music...")
#
#             elif "the time" in query:
#                 hour = datetime.datetime.now().strftime("%H")
#                 min = datetime.datetime.now().strftime("%M")
#                 say(f"Sir time is {hour} hours and {min} minutes")
#
#
#
#             elif "Using artificial intelligence".lower() in query.lower():
#                 ai(prompt=query)
#
#             elif "Jarvis Quit".lower() in query.lower():
#                 exit()
#
#             elif "reset chat".lower() in query.lower():
#                 chatStr = ""
#
#             else:
#                 print("Chatting...")
#                 chat(query)
















