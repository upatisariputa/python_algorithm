# 두  리스트  합치기
# 오름차순으로  정렬이  된  두  리스트가  주어지면  
# 두  리스트를  오름차순으로  합쳐  출력하는  프로그램을  작성하세요.
# sort 함수를 사용하지 마시오
# ▣입력설명
# 첫  번째  줄에  첫  번째  리스트의  크기  N(1<=N<=100)이  주어집니다.
# 두  번째  줄에  N개의  리스트  원소가  오름차순으로  주어집니다. 
# 세  번째  줄에  두  번째  리스트의  크기  M(1<=M<=100)이  주어집니다.
# 네  번째  줄에  M개의  리스트  원소가  오름차순으로  주어집니다. 
# 각  리스트의  원소는  int형  변수의  크기를  넘지  않습니다.
# ▣출력설명
# 오름차순으로  정렬된  리스트를  출력합니다.
# ▣입력예제  1                                                                     
# 3
# 1  3  5
# 5
# 2  3  6  7  9
# ▣출력예제  1
# 1  2  3  3  5  6  7  9

import os
import sys
import time
import re

path="./4/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()



def calculate (input_list):
  # plus_list= input_list[1] + input_list[3]
  # max_number = 0
  # min_number = 0
  # result_list =[]
  # if input_list[1][input_list[0]] > input_list[3][input_list[2]]:
  #   max_number = input_list[1][input_list[0]]
  # else:
  #   max_number = input_list[3][input_list[2]]
  # if input_list[1][input_list[0]] > input_list[3][input_list[2]]:
  #   min_number = input_list[3][input_list[2]]
  # else:
  #   min_number = input_list[1][input_list[0]]
  # result_list.append(min_number)
  # result_list.append(max_number)
  # for i in range(1, len(plus_list)-1):
  #   for j in plus_list:
  #     if j > plus_list[i] and j < plus_list[i+1]:
  #       result_list.insert(i, j)
  #     else 
  print()
    

def algorithm (n, a, m, b):
  p1=p2=0
  c=[]
  while p1<n and p2<m:
    if a[p1] <= b[p2]:
      c.append(a[p1])
      p1+=1
    else:
      c.append(b[p2])
      p2+=1
  if p1<n:
    c=c+a[p1:]
  if p2<m:
    c=c+b[p2:]
  print(c)


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  a = list(map(int, input().split()))
  m = int(input())
  b = list(map(int, input().split()))
  algorithm(n, a, m, b)
  # print(answer)


print('실행시간 :', time.time() - start)
  


