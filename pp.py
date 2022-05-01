from cgitb import text
import pyttsx3
import speech_recognition as sr
import yagmail
wel=pyttsx3.init()
voices =wel.getproprty('voices')
recognizer=sr.Recognizer()
print(voices)