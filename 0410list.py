""" msg="hello"
for i in msg:
    print(i) """
    
    
    
""" msg="hello"
num=1
for i in msg:
    print(num,'->',i)
    num += 1 """
    
    
""" score=[90,80,70,95]
print(score[-4])
print(score[-1])
print(score[0])
print(score[0:3])
print(score[-4:-1])
print(score[:2]) #
print(score[1:]) #0 다음 1부터 쭉 출력
print(score[:])  #전체 다
print(score[0:4:2])
print(score[-4:4:2])
print(score[-4:-1:2])
 """
 
""" score=[i for i in range(10)]
print(score)
# score=[i for i in range(10)]
 """
""" 
score=[10,20,30]
print(score)
score.sort()
print(score)
score.sort(reverse=True)
print(score)

print(max(score))   #가장 큰 수
print(min(score))   #가장 작은 수   
print(len(score))   #길이
print(sum(score))   #합
 """

""" a={10,20,30}
b={7,20,9}
c=a.union(b)    #합집합
print(c)

d=a.intersection(b)  #교집합
print(d)

e=a.symmetric_difference(b) #대칭자//둘 중 한 집합에는 속하지만 둘 모두에는 속하지는 않는 원소들의 집합
print(e)

f=a.difference(b)   #차집합
print(f) """

mount = {"mo1":"무등산","mo2":"영취산"}
print(mount["mo1"])
for i in mount:
    print(i)
    
for i,j in mount.items():
    print(i,j)
    
for i in mount.keys():
    print(i)
    
for j in mount.values():
    print(j)