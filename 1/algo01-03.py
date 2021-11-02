a=[0]*10 #일차원 리스트 생성
print(a)

a=[[0]*3 for _ in range(3)] # 이차원 리스트 생성 - 표로 생각할것
print(a)

a[0][1] = 1
print(a)

a[1][1] = 2
print(a)

for x in a:
  print(x)

for x in a:
  for y in x:
    print(y, end=' ')

  