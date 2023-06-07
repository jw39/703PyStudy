import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("듣고있어요")
    audio = r.listen(source)
    
try:
    text = r.recognize_google(audio, language="ko")  #소리를 집어넣으면 한국말 패치
    print('나: '+ text)
    
except sr.UnknownValueError:
    print('인식 실패')
except sr.RequestError as e:
    print('요청 실패: {0}'.format(e))