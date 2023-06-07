from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import openai
import random #random 어디감

openai.api_key = "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"

messages=[]

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ko')
        print('나 : ' + text)

    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e))

    user_content = text
    messages.append({"role" : "user", "content" : f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role" : "assistant", "content" : f"{assistant_content}"})

    print(f"GPT : {assistant_content}")

    file_name = 'sample.mp3'
    tts_ko = gTTS(text=assistant_content, lang='ko')
    tts_ko.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

    if '종료' in user_content:
            break
        
        
