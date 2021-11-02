a=[23, 13, 45, 32, 68]
print(a[:3]) #시작이 없으면 0번 부터
print(a[1:4]) 

print(len(a))

for i in range(len(a)):
  print(a[i], end=' ')

print()

for x in a:
  if x%2==1:
    print(x, end=' ')
print()  

# 
for x in enumerate(a):
  print(x, end=' ')
print()

b=(1,2,3,4,5) 
print(b[0])
# b[0]=7 # 튜플값은 변경 불가

for x in enumerate(a):
  print(x[0], x[1])
print()

for index, value in enumerate(a):
  print(index, value)
print()

if all(60>x for x in a): #all이라는 함수는 모두 참이여야 참이 나온다
  print('YES')
else:
  print('NO')

if any(60>x for x in a): #any 함수는 한번이라도 참이면 참
  print('YES')
else:
  print('NO')

