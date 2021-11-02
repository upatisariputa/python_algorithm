def plus_one(x):
  return x+1

print(plus_one(1))

plus_two = lambda x: x+2
print(plus_two(1))

# 람다함수- 내장함수의 인자함수로 사용될때 편리함

a=[1,2,3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))
