""" # 문제 1
num=int(input("정수를 입력하세요"))
print(num+int(10))
 """
 
""" #문제2
a=int(input("a?"))
b=int(input("b?"))
c=int(input("c?"))
sum=a+b+c
avg=(a+b+c)/3
print(a,b,c,sum,avg) """

""" #문제3
x=int(input("x?"))
print(3*x+4) """

""" #Q4
m=int(input("m?"))
print(m*60) """

# #Q5
# s=int(input("s?"))
# print(s)

""" #Q6
for i in range(5):
    for j in range(5):
        if j <= i:
            print("*",end="")
    print() """
    
    
""" #Q7
x=int(input("x?"))
for i in range(x):
    for j in range(x):
        if j <= i:
            print("*", end="")
    print() """

""" #Q8
letters="python"
print(letters[0:4:2]) """

""" #Q9
license_plate="24가 2210"
print(license_plate[4:]) """

""" #Q10
string="홀짝홀짝홀짝"
print(string[0::2])
 """
 
""" #Q11
string="PYTHON"
print(string[::-1]) """

""" #Q12
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)
 """
 
""" # #Q13
lang1={"C","C++","JAVA"}
lang2={"Python", "GO", "C#"}
langs=lang1.union(lang2)
print(langs)
//langs = lang1 + lang2
//print(langs)
 """


""" #Q14
nums=[1,2.3,4,5,6,7]
print(min(nums))
print(max(nums))
 """
 
""" #Q15
nums = [1,2,3,4,5]
print(sum(nums)) """

#Q16
#1번째 방법
""" cook=["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소세지","라면","팥빙수","김치전"]
count = len(cook)
print(count)

#2번째 방법
def count(lst):
    return len(lst)

cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소세지","라면","팥빙수","김치전"]
count = count(cook)
print(count) """


""" 
#Q17
price = ["20180728", 100, 130, 140, 150, 160, 170]
print(price[1:]) """


""" #Q18
a=3.5
b=int(3.5)
print(a**((a//b)*2))
print(((a-b)*a)//b)
b=(((a-b)*a)%b)
print(b)
print((a*4)%(b*4))
 """

#Q19
""" a='3'
b=float(a)
print(b**int(a)) """

""" a=[0,1,2,3,4]
print(a[:3],a[:-3]) """

#Q20
""" a=[0,1,2,3,4]
print(a[::-1])
->[4, 3, 2, 1, 0] """

""" #Q21
a=[0,1,2,3,4]
print(a[::-1]) """

""" #Q22
num = [1,2,3,4]
print(num*2) """

""" #Q23
def add_and_mul(a,b,c):
    return b+a*c+b
print(add_and_mul(3,4,5)== 63) """

""" #Q24
def welcome():
    print("환영합니다")
for i in range(3):
    welcome()
 """

##########################################
""" #Q1
name=input("이름?")
def welcome(name):
    print("환영합니다"+name+"님")
welcome(name) """

#Q2
""" def print_str(string,count):
    for i in range(count):
        print(string)
        
print_str("파이썬", 3) """

 #Q3
""" def welcome(name, msg="환영합니다"):
    print(msg, name + "님")
    
welcome("지원")
welcome("지원", "반갑습니다")
 """


""" #Q4
def circle_area(radius):
    area = 3.141592 * radius ** 2
    return area

radius = int(input("반지름은?"))
area = circle_area(radius)
print(f"반지름이 {radius}인 원의 넓이는 {area}입니다.") """

""" #Q5
def pow_xy(x, y):
    return x ** y

result = 3 * pow_xy(2, 4) + 5
print(result)
 """
 
"""  #Q6
def pzn(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1

while True:
    num = int(input("정수를 입력하세요: "))
    result = pzn(num)
    if result == 1:
        print("양수")
    elif result == -1:
        print("음수")
    else:
        print("0")
        break """
        
#Q7
""" def vsum(*args):
    total = 0
    for num in args:
        total += num
    return total
# result = vsum(1, 2, 3)
# print(result)  # 출력결과: 6

print(vsum(2, 3))          # 결과: 5
print(vsum(2, 3, 4))       # 결과: 9
print(vsum(2, 3, 4, 5))  """

""" #Q8
a=11
b=9
print('a'+'b') """

""" #Q9
a="abcd e f g"
b=a.split()
c=(a[:3][0])
d=(b[:3][0][0])
print(c+d) """