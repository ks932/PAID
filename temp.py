import speech_recognition as sr
import pyaudio
import pyttsx3

try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initialize')
    
voices = engine.getProperty('voices')

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_frFR_JulieM')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


r=sr.Recognizer()

speak_text_cmd('Bonjour, je suis MaÏa ton Intelligence artificielle je vais pouvoir t\'aider')

x = True

with sr.Microphone() as source:
    while x == True:
        r.adjust_for_ambient_noise(source,duration=1)
        print("say anything : ")
        audio= r.listen(source)
        try:
            text = r.recognize_google(audio, language="fr-FR")
            print(text)
            if 'au revoir' in text:
                speak_text_cmd('Aurevoir à bientôt !')
                x = False
            elif 'pas bien' in text:
                speak_text_cmd('as-tu mal à la tête ?')
                continue
            elif 'bonjour' in text:
                speak_text_cmd('bonjour, comment puis-je vous aider ?')
                continue
            else:
                speak_text_cmd(text)
        except:
            print("sorry, could not recognise")
