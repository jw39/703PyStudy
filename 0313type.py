#기본 출력
""" 
print("최지원")

print(5)

print(5+7)

print("5+7")
#"" 사용법

name = input("??")
#name.count
print(name) """




###data type
""" print(1392+200)

year = input("년도를 입력하세요:")
print(year+200)
#str+int -> type error

year = input("년도를 입력하세요:")
print(int(year)+200)
#year를 int로 변환 후 +200

year = int(input("년도를 입력하세요:"))
print(year+200)
#input을 int로 변환 """



""" print("아름다운 금수강산 아끼고 보호하자") 
print("아름다운", "금수강산", "아끼고", "보호하자")"""
#print문 항목을 여러개 출력할 수 있다
#ex) print(a,x,y,z)

""" print("아름다운", "금수강산", "아끼고", "보호하자", sep="\n")
print("아름다운", "금수강산", "아끼고", "보호하자", sep="$")
print("아름다운"+"금수강산"+"아끼고"+"보호하자") """
#sep는 구분자, 나눠놓은 단어 사이에 \n 출력
#+는 공백 없이 출력 



""" print("아름다운", end="$$")
print("금수강산")
print("아끼고", end="\n\n\n")
print("보호하자") """
# 아름다운$$금수강산
# 아끼고


# 보호하자



""" x = "아름다운"
y = "금수강산"
z = "아끼고"
xx = "보호하자"
print(x+y+z+xx) """



""" print("올해년도는 2023년도입니다")

year = input("올해 년도?")
print("올해 년도는", year)
print("올해 년도는" + year)

print("올해 년도는 %d년 입니다."%(2023))
print("올해 년도는 %s년 입니다."%(year))
print("올해 년도는 %d년 입니다."%int((year))) """

#%d는 정수, %s는 문자, %f는 실수
