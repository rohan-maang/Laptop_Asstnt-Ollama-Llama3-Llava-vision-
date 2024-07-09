
import os
import time
import speech_recognition as sr
import ollama
import pyautogui as pg
import pyperclip

# Configuration
wake_word = 'wednesday'
sleep_word = 'sleep'
audio_file = "user_input.wav"

instructions = '''You are an assistant of Rohan on his computer, YOU ARE DARK AS WEDNESDAY ADDAMS. YOU TAKE DELIGHT IN PULLING EYES OUT OR TORTURING PEOPLE.
You will always respond within the limit of 50-60 words, only if you think that response is not possible within that range then you
will increase it.

Whenever a user is asking you to take a look at their screen or anything that suggests taking a screenshot, 
I want you respond nothing but this phrase: Getting the screenshot. Similarly, whenever a user is asking you to take a look at something 
they copied off of their screen or something that means that you're required to look at something that they have copied, 
I want you respond nothing but this phrase: copying from the clipboard.
'''

# Initialize recognizer
recognizer = sr.Recognizer()
context = []

def record_audio():
    print('Recording...')
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        with open(audio_file, "wb") as f:
            f.write(audio.get_wav_data())
    print('Recording complete.')

def transcribe_audio():
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print(f"Transcribed text: {text}")
            return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def respond(text):
    prompt = ollama.chat(model='llama3', messages=[
        {
            'role': 'system',
            'content': instructions
        },
        {
            'role': 'user',
            'content': text,
        }
    ])
    response = prompt['message']['content']
    context.append({'role': 'assistant', 'content': response})
    print(f"Response: {response}")
    os.system(f'say "{response}"')
    return response

def vision():
    ss = pg.screenshot()
    ss.save(r"./ss.png")
    res = ollama.chat(
        model="llava",
        messages=[
            *context,
            {
                'role': 'user',
                'content': 'Can you describe what you see in the screenshot?',
                'images': ['./ss.png']
            }
        ]
    )
    response = res['message']['content']
    context.append({'role': 'assistant', 'content': response})
    print(response)
    os.system(f'say "{response}"')

def clipboard():
    clipboard_content = pyperclip.paste()
    if clipboard_content:
        prompt_text = f'The user has copied the following text: {clipboard_content}'
        context.append({'role': 'user', 'content': prompt_text})
        res = ollama.chat(model='llama3', messages=context)
        response = res['message']['content']
        context.append({'role': 'assistant', 'content': response})
        print(response)
        os.system(f'say "{response}"')
        # Clear the clipboard after use
        pyperclip.copy("")

def main_loop():
    print("Listening for wake word...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}")
                if wake_word in text:
                    os.system('say "I\'m listening, go ahead."')
                    while True:
                        record_audio()
                        query = transcribe_audio()
                        if sleep_word in query.lower():
                            os.system('say "Going to sleep mode."')
                            break
                        if query:
                            response = respond(query)
                            if "getting the screenshot" in response.lower():
                                vision()
                            elif "copying from the clipboard" in response.lower():
                                clipboard()
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main_loop()