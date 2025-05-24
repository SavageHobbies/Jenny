# My Simple Assistant

This is a simple command-line assistant that can perform basic tasks using voice commands and provides spoken responses.

## Dependencies

This assistant relies on the following Python libraries:

- `SpeechRecognition`: For recognizing voice commands.
- `pyttsx3`: For text-to-speech output.

These will be installed automatically when you run:
```bash
pip install -r requirements.txt
```

**System Dependencies:**
- **Microphone Input (`SpeechRecognition` via `PyAudio`):** You may need to install system libraries for `PyAudio` (which `SpeechRecognition` uses for microphone access). On Debian/Ubuntu, this is typically `portaudio19-dev`.
  ```bash
  sudo apt-get install portaudio19-dev 
  ```
- **Text-to-Speech (`pyttsx3`):** `pyttsx3` may require a TTS engine to be installed on your system. For Linux, `espeak` is a common option.
  ```bash
  sudo apt-get install espeak
  ```
  Other operating systems might have different requirements or pre-installed TTS engines.

## How to Run

**Hardware Requirements:**
- A working microphone is required for voice input.
- Speakers or headphones are required for voice output.

**Running the Assistant:**
1. Ensure you have installed the dependencies as mentioned above (both Python and system).
2. Execute the following command in your terminal:

```bash
python assistant.py
```
The assistant will then be listening for your voice commands.

## Available Commands

The assistant understands the following voice commands:

- `"hello"`: Greets the user.
- `"time"`: Displays and speaks the current date and time.
- `"exit"` or `"quit"`: Exits the assistant.

Simply say the command when the assistant is listening.
