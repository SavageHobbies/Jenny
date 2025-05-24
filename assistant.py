# Manual Testing Notes:
# 1. Ensure your microphone is connected and configured as the default system input.
# 2. Run the assistant: `python assistant.py`.
# 3. When "Assistant: Listening..." appears, say a command like 'hello' or 'time'.
# 4. Verify that the assistant recognizes your speech and responds audibly.
# 5. Troubleshooting tips:
#    - Check microphone levels in your system settings.
#    - Ensure no other application is exclusively using the microphone.
#    - Verify system dependencies like PortAudio (for SpeechRecognition) and
#      a TTS engine like espeak (for pyttsx3) are correctly installed if issues arise.
#    - Check `requirements.txt` for Python package dependencies.

import datetime
import speech_recognition as sr
import pyttsx3

print("--- Speech Setup Check ---")
try:
    mic_names = sr.Microphone.list_microphone_names()
    if mic_names:
        print("Available microphones:")
        for index, name in enumerate(mic_names):
            print(f"  Mic #{index}: {name}")
    else:
        print("No microphones found.")
except Exception as e:
    print(f"Error listing microphones: {e}")
print("--------------------------")

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error during speech output: {e}")

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # This print is more of a system status, not a direct assistant response to a command.
        # The subtask asks to replace "user-facing print statements from the assistant".
        # Let's assume "Listening..." and "Recognizing..." are status updates and keep them as print.
        # However, the error messages below are direct feedback from the assistant.
        print("Assistant: Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source)
            print("Assistant: Recognizing...") # Status update
            command = r.recognize_google(audio).lower()
            print(f"You said: {command}") # Log of user input, not assistant response
            return command
        except sr.UnknownValueError:
            speak("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            speak(f"An unexpected error occurred during speech recognition: {e}")
            return None

def process_command(command):
    if command == "hello":
        speak("Hello there!")
    elif command == "time":
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        speak(f"Unknown command: {command}")

def main():
    speak("Welcome to your new assistant!") # Changed from print
    while True:
        try:
            user_input = listen_for_command()
            if user_input:
                if user_input in ["exit", "quit"]:
                    speak("Goodbye!") # Changed from print
                    break
                process_command(user_input)
        except KeyboardInterrupt:
            speak("\nGoodbye!") # Changed from print
            break
        except Exception as e:
            speak(f"An error occurred: {e}") # Changed from print

if __name__ == "__main__":
    main()
