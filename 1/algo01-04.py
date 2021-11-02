def add(a, b):
  c=a+b
  print(c)

add(4,65)
add(5,51)

def add(a,b):
  c=a+b
  return c

d= add(3,5)
print(d)

def add(a,b):
  c = a+b
  d = a-b
  return c, d #리턴을 여러개 가능, 튜플로 반환

print(add(5,4))

def isPrime(x):
  for i in range(2, x):
    if x%i==0:
      return False
  return True

a=[12,13,6,7,16]

for x in a:
  if isPrime(x):
    print(x, end=' ')


