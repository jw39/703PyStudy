""" 
sum=0
i=1
for x in range(10):
    sum=sum+i
    print(i,sum)
    i=i+1
print(sum)
    
     """
#range 몇 번 반복해라 하는 함수 , range 뒤에도 :, 들여쓰기 중요
#0에서 부터 시작해서 for앞으로 들어감, 



# for x in range(1,101,2):
#     print(x)

# while(True):
#     x=input("x:")
#     y=input("y:")
#     z=input("z:")
#     for i in range(x,y,z):
#         print(x)

""" while(True):
    #s,e,st=input("s,e,st?").split()
    s,e,st=map(int, input("s,e,st?").split())   # map 함수
    # s=int(s)
    # e=int(e)
    # st=int(st)
    sum=0
    for i in range(s, e+1, st):
        sum+=i
        print(i,sum) """
        

# for i in range(1,10):
#     print("2*%2d=%3d"%(i,2*i))
    
# for x in range(2,10): 
#     for y in range(1,10):
#         print(x, '*', y, '=', x * y)
#         if(y == 9):
#             print('----------')

# print("구구단 출력")
# for x in range(2, 10):
#     print("-----------")
#     for y in range(1, 10):
#         print(x, "x", y, "=", x*y)

for x in range(1,10): 
    for y in range(2,10):
        print(y, "*", x, '=',  x* y, end = '\t')  
    print()