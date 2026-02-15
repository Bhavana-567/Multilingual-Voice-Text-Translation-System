import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Language dictionary
languages = {
    "english": "en",
    "hindi": "hi",
    "telugu": "te",
    "tamil": "ta",
    "kannada": "kn"
}

recognizer = sr.Recognizer()
translator = Translator()

def speech_to_text(source_lang):
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language=source_lang)
            print("📝 Recognized Text:", text)
            return text
        except:
            print("❌ Could not understand audio")
            return None

def translate_text(text, target_lang):
    translated = translator.translate(text, dest=target_lang)
    print("🌍 Translated Text:", translated.text)
    return translated.text

def text_to_speech(text, lang_code):
    tts = gTTS(text=text, lang=lang_code)
    tts.save("output.mp3")
    os.system("start output.mp3")  # For Windows

def main():
    print("Available Languages: English, Hindi, Telugu, Tamil, Kannada")

    source = input("Enter source language: ").lower()
    target = input("Enter target language: ").lower()

    if source not in languages or target not in languages:
        print("❌ Language not supported")
        return

    source_code = languages[source]
    target_code = languages[target]

    text = speech_to_text(source_code)

    if text:
        translated_text = translate_text(text, target_code)
        text_to_speech(translated_text, target_code)

if __name__ == "__main__":
    main()
