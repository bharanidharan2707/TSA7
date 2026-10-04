import speech_recognition as sr
from deep_translator import GoogleTranslator

def translate_speech(target_language='es'):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening... Speak now.")
            
            # Listen to the user's speech
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
            print("Processing speech...")

        # Convert speech to text (defaulting to English for input, but it can be changed)
        text = recognizer.recognize_google(audio)
        print(f"\nOriginal Text: {text}")

        # Translate the text
        translator = GoogleTranslator(source='auto', target=target_language)
        translated_text = translator.translate(text)
        
        print(f"Translated Text ({target_language}): {translated_text}")

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Python Speech Translator!")
    print("Supported languages include: 'es' (Spanish), 'fr' (French), 'de' (German), 'hi' (Hindi), 'ja' (Japanese), etc.")
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish, 'fr' for French): ").strip()
    
    if not target_lang:
        target_lang = 'es'
        print("No language code entered. Defaulting to Spanish ('es').")
    
    try:
        translate_speech(target_language=target_lang)
    except KeyboardInterrupt:
        print("\nExiting translator.")
