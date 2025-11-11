import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for i, v in enumerate(voices):
    print(i, v.name)

# Example: choose Indian English female voice if available
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 165)  # speaking speed

engine.say("Hello! Welcome to the Smart Crop Prediction System.")
engine.runAndWait()
