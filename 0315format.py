# p=3.14
# r=10
# print("%d"%(2*p*r))

""" format 기초
p=3.14
r= 10 #int(input("반지름을 입력하세요"))
print("반지름 %d인 원의 둘레는 %d입니다."%(r,2*p*r))
#d,s,f
print("{}".format(r)) """

#사용법
#{} 한 후 .format //(!.format) 
# 객체(문자열)이 가지고 있는 속성 중 format은 format 다음()의 값을 {}에다가 불러올 수 있다.

""" format 응용
print("1->{}, 2->{}".format(r,p))
print("1->{0}, 2->{1}".format(r,p))
print("1->{1}, 2->{0}".format(r,p))
print("1->{1}, 2->{0},3->{1}, 4->{0}".format(r,p))
print("1->{1}, 2->{0},3->{a}, 4->{0}".format(r,p, a="장어"))
두개도 사용 가능. 순서 바꿔서도 사용 가능, 인덱스에 변수 넣어서 뒤에 변수의 값을 지정하면 그대로 출력
 """

#print("안녕하세요{} 오늘은".format("주인님"))

print("%s"%("살구"), end="")
print(type("나무"))
print("%10s"%("살구"), end="")
print(type("나무"))
print("%-10s"%("살구"), end="")
print(type("나무"))

# print(type(p))
# print(type(r))

# 살구나무
#         살구나무
# 살구        나무  -> 왜 이렇게 출력??
#type은 str인지 int인지 확인할 수 있다

