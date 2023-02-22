import pyttsx3 as tts
import keyboard

isSpeaking = False
ttsEngine = tts.init()

while True:
    if keyboard.is_pressed("1"):
        ttsEngine.say("Hi!  My name is Herbie Aureum and I am a plantpreneur, and CEO of Plantiverse, working together with Cecilia and her team at Futurity Systems to build an interspecies economy. We will be at BEAT Barcelona if anybody wants to get to know me better, I will be there to answer any questions, you can see me in real life, in VR and AR and you will even have a chance to buy one of my NFTrees!  You will just have to come and find out more.")
        ttsEngine.runAndWait()


    
        