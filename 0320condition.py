""" 
x=int(input("x?"))
if(x%2)==0:
    print("짝수")
else:
    print("홀수")

print("x=",x)

"""


#if문 작성 후에는 : 과 들여쓰기 필수
#elif 는 '그리고' 개념 이 조건 그리고 다음 조건 그리고 다다음 조건~,,

""" 
ID="jiwon"
PW="jjjj"

id=input("id를 입력하세요")
pw=input("pw를 입력하세요")
if(ID==id):
    print("id ok")
else:
    print("go back")
if(PW==pw):
    print("pw ok")
else:
    print("go back")
 """

#if문 하나로 줄이기 //and사용해서 두 값 모두 참일 때 ok,아니면 go back
ID="jiwon"
PW="jjjj"
id=input("id를 입력하세요")
pw=input("pw를 입력하세요")

id=input("id를 입력하세요")
pw=input("pw를 입력하세요")
if((ID==id) and (PW==pw)):
    print("ok")
else:
    print("go back")



""" 
중첩 if문 사용해 아이디 비번 입력
if(ID==id):
    if(PW==pw):
        print("ok")
    else:
        print("go back")
else:
    print("fail") """


