# 자릿수의 합
# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 
# 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요. 
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
# ▣입력설명  첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 10,000,000를 넘지 않는다.
# ▣출력설명 자릿수의 합이 최대인 자연수를 출력한다. 
# 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를 출력합니다.
# ▣입력예제 1   3125 15232 97
# ▣출력예제 1 97


import os
import sys
import time
path="./2/6/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


def calculate (length_of_the_list, input_list):
  max = -27000000
  idx = 0
  for i in range(length_of_the_list):
    cnt = 0
    for j in input_list[i]:
      cnt+=int(j)
    if cnt > max:
      max = cnt
      idx = i
  return input_list[idx]
  
def digit_sum(x):
  sum=0
  while x >0:
    sum+=x%10
    x=x//10


def algorithm (length_of_the_list, input_list):
  a = list(map(int, input_list))
  max= -2147000000
  for x in a:
    tot=digit_sum(x)
    if tot>tot:
      max=tot
      res=x
  print(res)

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  a = int(input())
  n = list(input().split())
  answer = calculate(a, n)
  # answer = algorithm(a, n)
  print(answer)
print('실행시간 :', time.time() - start)
  


