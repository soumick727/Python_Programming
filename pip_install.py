# first we have to install a module in the terminal with the help of pip 
# module name is pyttsx3
import pyttsx3, pyjokes

engine = pyttsx3.init()
engine.say("Hi my name is soumick roy and I am a python programmer")
engine.runAndWait()

# Get a random joke using pyjokes
p = pyjokes.get_joke()
print(p)