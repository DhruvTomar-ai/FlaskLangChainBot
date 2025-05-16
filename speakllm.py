import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()



# import pyttsx3

# try:
#     engine = pyttsx3.init()

#     # ✅ List available voices
#     voices = engine.getProperty('voices')
#     print(f"🔊 Found {len(voices)} voice(s):")
#     for idx, voice in enumerate(voices):
#         print(f"{idx}: {voice.name} ({voice.languages}) - {voice.id}")

#     # ✅ Try speaking with the first voice
#     engine.setProperty('voice', voices[0].id)
#     engine.setProperty('rate', 150)
#     engine.say("Hello, this is a test message.")
#     engine.runAndWait()

# except Exception as e:
#     print("❌ Error with pyttsx3:", e)
