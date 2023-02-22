import pyttsx3 as tts
import keyboard

isSpeaking = False
ttsEngine = tts.init()

while True:
    if keyboard.is_pressed("1"):
        ttsEngine.say("this is when herbie will speak")
        ttsEngine.runAndWait()


    
        