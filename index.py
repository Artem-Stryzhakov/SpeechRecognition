import speech_recognition as sr
import openai, gtts, os
from playsound import playsound

recognition = sr.Recognizer()
mic = sr.Microphone()

openai.api_key = "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"

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

def launchAudioAnswer(answer):
    tts = gtts.gTTS(answer, lang="en")
    tts.save("gptAnswer.mp3")
    playsound("gptAnswer.mp3")
    os.remove("gptAnswer.mp3")

def chatGptAnswer():
    print("Speak:")

    with mic as source:
        audio = recognition.listen(source)

    try:
        text = recognition.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Unable to recognize your speech. Try again or check your microphone")

    try:
        messages.append(
            {"role": "user", "content": text},
        )
    except UnboundLocalError:
        pass

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )
    reply = chat.choices[0].message.content

    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    launchAudioAnswer(reply)

'''while True:
    print("Speak:")

    with mic as source:
        audio = recognition.listen(source)

    try:
        text = recognition.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Unable to recognize your speech. Try again or check your microphone")

    try:
        messages.append(
            {"role": "user", "content": text},
        )
    except UnboundLocalError:
        pass

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )
    reply = chat.choices[0].message.content

    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    launchAudioAnswer(reply)
    if text.lower() == "thank you" or text.lower() == "thanks":
        break'''