
# from gtts import gTTS
# from playsound import playsound
# import threading
# import os
# import uuid

# def speak(text):
#     def run():
#         try:
#             filename = f"voice_{uuid.uuid4()}.mp3"
#             tts = gTTS(text=text, lang='en')
#             tts.save(filename)
#             playsound(filename)
#             os.remove(filename)
#         except Exception as e:
#             print("Voice error:", e)
#     threading.Thread(target=run).start()
# from gtts import gTTS
# from playsound import playsound
# import threading
# import os
# import uuid
# import speech_recognition as sr

# def speak(text):
#     def run():
#         try:
#             filename = f"voice_{uuid.uuid4()}.mp3"
#             tts = gTTS(text=text, lang='en')
#             tts.save(filename)
#             playsound(filename)
#             os.remove(filename)
#         except Exception as e:
#             print("Voice error:", e)
#     threading.Thread(target=run).start()

# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening now...")
#         print("Listening...")
#         try:
#             audio = r.listen(source, timeout=5)
#             query = r.recognize_google(audio)
#             return query
#         except Exception as e:
#             speak("Sorry, I didn't catch that.")
#             return ""
from gtts import gTTS
from playsound import playsound
import threading
import os
import uuid
import speech_recognition as sr

def speak(text):
    def run():
        try:
            filename = f"voice_{uuid.uuid4()}.mp3"
            tts = gTTS(text=text, lang='en')
            tts.save(filename)
            playsound(filename)
            os.remove(filename)
        except Exception as e:
            print("Voice error:", e)
    threading.Thread(target=run).start()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening now...")
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5)
            return r.recognize_google(audio)
        except:
            speak("Sorry, I didn't catch that.")
            return ""
