# 뒤집은 소수
# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 
# 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 
# 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다. 
# 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 
# def isPrime(x)를 반드시 작성하여 프로그래밍 한다.
# ▣입력설명
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
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
path="./8/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def reverse(target_number):
  number_to_string=str(target_number)
  reverse_number=int(number_to_string[::-1])
  abs_number=abs(reverse_number)
  return abs_number

def isPrime(target_number):
  for i in range(2, target_number):
    if(target_number%i==0):
      return False
  return True

def calculate(b):
  result_list=[]
  reversed_number_list=[]
  for i in b:
    reversed_number_list.append(reverse(i))
  for j in reversed_number_list:
    if(isPrime(j) and j!=1):
      result_list.append(j)
  print(result_list)


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  a = int(input())
  b = list(map(int, input().split()))
  calculate(b)

print('실행시간 :', time.time() - start)
  


