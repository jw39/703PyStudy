import random
import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import openai

# OpenAI API 인증키 설정
openai.api_key = "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"

# 대화를 저장할 리스트
conversation = []

# 챗봇의 초기 인사
initial_message = "안녕하세요, 무엇을 도와드릴까요?"
conversation.append({"role": "assistant", "content": initial_message})

# 미리 생성된 대답 리스트
predefined_responses = [
    "네, 알겠습니다.",
    "그럴 수 있습니다.",
    "해당 정보를 찾아보겠습니다.",
    "정확한 답변을 드리기 위해 좀 더 자세한 내용을 알려주세요.",
    "죄송합니다, 제가 이해할 수 없는 내용 같아요."
]

while True:

    # 사용자의 음성 입력 인식
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # 인식된 음성을 텍스트로 변환
        user_input = r.recognize_google(audio, language='ko')
        print('사용자: ' + user_input)

    except sr.UnknownValueError:
        print('음성을 인식하지 못했습니다.')
        continue
    except sr.RequestError as e:
        print('오류 발생: {0}'.format(e))
        continue

    # 대화 기록에 사용자의 발화 추가
    conversation.append({"role": "user", "content": user_input})

    # 미리 생성된 대답 중 랜덤으로 선택
    predefined_response = random.choice(predefined_responses)

    # OpenAI API를 사용하여 챗봇의 대답 생성
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='\n'.join([f"{c['role']}: {c['content']}" for c in conversation]),
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 챗봇의 대답을 대화 기록에 추가
    bot_response = response.choices[0].text.strip()
    conversation.append({"role": "assistant", "content": bot_response})

    print(f"챗봇: {bot_response}")

    # 챗봇의 음성 출력
    file_name = 'response.mp3'
    tts = gTTS(text=bot_response, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)

    # 사용자가 '종료'라고 말하면 대화 종료
    if '종료' in user_input:
        break