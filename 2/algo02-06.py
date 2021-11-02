# 소수(에라토스테네스 체)
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다. ▣입력설명첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
# ▣출력설명 첫 줄에 소수의 개수를 출력합니다. 
# ▣입력예제 1  20
# ▣출력예제 18


import os
import sys
import time
path="./2/7/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


def calculate (input_number):
  # cnt = 0
  # prime_number_list = list(range(2, input_number+1))
  # for i in range(2, input_number+1):
  #   for j in range(2, input_number):
  #     if i%j==0:
  #       prime_number_list.remove(i)
  return False


def algorithm (input_number):
  if input_number==2:
    return 1
  ch=[0]*(input_number+1)
  cnt=0
  for i in range(2, input_number):
    if ch[i]==0:
      cnt+=1
      for j in range(i, input_number+1, i):
        ch[j]=1
  return cnt

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  a = int(input())
  # answer = calculate(a)
  answer = algorithm(a)
  print(answer)
print('실행시간 :', time.time() - start)
  


