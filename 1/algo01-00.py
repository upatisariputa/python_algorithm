# 이중 반복문
print('- 이중 반복문')
for i in range(5):
  for j in range(i + 1):
    print('*', end=' ')
  print()


for i in range(5):
  for j in range(5-i):
    print('$', end=' ')
  print()

print('- 문자열과 내장함수', sep=' ')

# 문자열과 내장함수
msg = 'It is Time'
print(msg.upper())
print(msg.lower())

tmp = msg.upper()
print(tmp)
print(tmp.find('T')) #첫번째 인덱스 번호
print(tmp.count('T')) # 몇개 있는지?
print(msg[:2]) # slice
print(msg[3:5])
print(len(msg)) #length
for i in range(len(msg)):
  print(msg[i], end=' ')
print()
for x in msg:
  print(x, end=' ')
print()
for x in msg:
  if x.isupper():
    print(x, end=' ')
print()
for x in msg: 
  if x.islower():
    print(x, end=' ')
for x in msg:
  if x.isalpha():
    print(x, end=' ')
print()
tmp='AZ'
for x in tmp:
  print(ord(x), end=' ')
print()
tmp='az'
for x in tmp:
  print(ord(x), end=' ')
print()
tmp=65
print(chr(tmp))
print()


# 리스트와 내장함수
