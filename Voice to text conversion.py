#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install Flask SpeechRecognition pyaudio


# In[2]:


import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()


# In[3]:


def recognize_speech_from_mic():
    # Obtain audio from the microphone
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        print("Transcribing audio...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


# In[4]:


# Example function to add a note (you can modify it according to your app's logic)
def add_note_from_speech():
    note_content = recognize_speech_from_mic()
    if note_content:
        # Assuming you have a function add_note that takes a title and content
        add_note("Speech Note", note_content)

# Example add_note function (replace this with your actual function)
def add_note(title, content):
    print(f"Adding note - Title: {title}, Content: {content}")

# Call the function to add a note from speech
add_note_from_speech()

