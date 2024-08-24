import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrery

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    if "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrery.music[song]
        webbrowser.open(link)
    
    else:
        speak("Sorry, I didn't understand that. Please try again.")

if __name__ == '__main__':
    speak('Initializing Jarvis...')
    
    while True:
        try:
            with sr.Microphone() as source:
                # obtain audio from the microphone
                print("Listening for wake word...")
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
                
                # Increased timeout and phrase_time_limit
                audio = r.listen(source, phrase_time_limit=3, timeout=5)

                # recognize speech using Google
                print("Recognizing...")
                word = r.recognize_google(audio)
                
                if word.lower() == "jarvis":
                    speak("Yes?")
                    
                    with sr.Microphone() as source:
                        print("Jarvis is listening...")
                        r.adjust_for_ambient_noise(source, duration=1)
                        audio = r.listen(source)

                    command = r.recognize_google(audio)
                    processCommand(command)
                    
        except sr.WaitTimeoutError:
            print("Listening timed out, please try again.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
