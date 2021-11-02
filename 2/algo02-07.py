# 뒤집은 소수
# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 
# 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다. 
# 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하여 프로그래밍 한다.
# ▣입력설명첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 100,000를 넘지 않는다.
# ▣출력설명
# 첫 줄에 뒤집은 소수를 출력합니다. 
# 출력순서는 입력된 순서대로 출력합니다.
# ▣입력예제 1 
# 32 55 62 3700 250
# ▣출력예제 1 
# 23 73


import os
import sys
import time
path="./2/8/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def reverse(input_list):
  f = []
  for i in input_list:
    f.append(i[::-1])
  f = list(map(int, f))
  return f
  

def isPrime(number):
  for i in range(2, number):
    if number%i==0:
      return False
  return True

def calculate (input_list):
  reversed_list = reverse(input_list)
  result_list=[]
  for i in reversed_list:
    if isPrime(i) and i!=1:
      result_list.append(i)
  return result_list

def reversed_algo(x):
  res=0
  while x>0:
    t=x%10
    res=res*10+t
    x=x//10
  return res

def isPrime_algo(number):
  if number==1:
    return False
  for i in range(2, number//2):
    if number%i==0:
      return False
  else:
    return True

def algorithm (input_number):
  for x in input_number:
    tmp=reversed_algo(x)
    if isPrime_algo(tmp):
      return tmp


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  b = int(input())
  # a = list(input().split())
  # answer = calculate(a)

  a = list(map(int, input().split()))
  answer = algorithm(a)
  print(answer)
print('실행시간 :', time.time() - start)
  


