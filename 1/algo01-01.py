import random as r

a=[]
#print(a)
b=list()
#print(b)

a=[1,2,3,4,5,]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)

c=a+b
#print(c)

a.append(6)
print(a)

a.insert(3, 7)

print(a)

a.pop()
print(a)

a.pop(3)
print(a)

a.remove(4)
print(a)

print(a.index(5)) # 5라는 값의 index를 출력

a=list(range(1,11))
print(a)

print(sum(a)) #a 리스트의 모든 값 더하기

print(max(a)) #a 리스트의 최대값

print(min(a)) #a 리스트의 최소값

print(min(7,5)) # (7,5)의 최소값

print(min(7,3,5))

print(a)

r.shuffle(a) # a를 섞어라
print(a) 
a.sort(reverse=True) # 내림차순
print(a)
a.sort() # 오름차순
print(a) 

a.clear() # 빈리스트
print(a)





