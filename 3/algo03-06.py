# 격자판  최대합
# 5*5  격자판에  아래롸  같이  숫자가  적혀있습니다. 
# 10 13 10 12 15 
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# N*N의  격자판이  주어지면  각  행의  합,  
# 각  열의  합,  두  대각선의  합  중  가  장  큰  합을  출력합니다.
# ▣입력설명
# 첫  줄에  자연수  N이  주어진다.(1<=N<=50) 
# 두  번째  줄부터  N줄에  걸쳐  각  줄에  N개의  자연수가  주어진다.  
# 각  자연수는  100을  넘지  않는다. 
# ▣출력설명최대합을  출력합니다.
# ▣입력예제  1                                                                    
# 5
# 10  13  10  12  15
# 12  39  30  23  11
# 11  25  50  53  15
# 19  27  29  37  27
# 19  13  30  13  19
# ▣출력예제  1
# 155

import os
import sys
import time
import re

path="./6/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def calculate (n, m):
  result = 0
  for i in range(n):
    if sum(m[i]) > result:
      result = sum(m[i])
  for i in range(n):
    sum_result = 0
    for j in range(n):
      sum_result += m[i][j]
    if sum_result > result:
      result = sum_result
  for i in range(n):
    sum_result1=0
    sum_result2=0
    for j in reversed(range(n)):
      sum_result1 += m[i][j]
      sum_result2 += m[j][i]
    if sum_result1 > result:
      result = sum_result1
    if sum_result2 > result:
      result = sum_result2
  print(result)
    

def algorithm ():
  print()


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  m = []
  for i in range(n):
    m.append(list(map(int, input().split())))
  # print(m)
  calculate(n, m)
  # algorithm(n,m)


print('실행시간 :', time.time() - start)