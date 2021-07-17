import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 190)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command(lan="pt-BR"):
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            engine.say("Estou ouvindo.")
            engine.runAndWait()

            voice = listener.listen(source)
            command = listener.recognize_google(voice, language=lan)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
            return command
    except:
        return False


def time_format_control():


def run_assistant():
    command = take_command()
    if not command:
        talk("Não entendi")
        return False

    if "play" in command:
        command = command.replace("Reproduzir", "")
        print("Reproduzindo: " + command)
        talk("Reproduzindo" + command)
        pywhatkit.playonyt(command)


    elif "Tchau" in command or "Fechar programa" in command:
        print("Tchau")
        talk("Tchau")

    else:
        talk("Não entendi. Espere um segundo e fale novamente.")
        return False


while True:
    run_assistant()
