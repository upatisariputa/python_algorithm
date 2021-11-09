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
# ▣출력설명
# 최대합을  출력합니다.
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

def calculate(n, m):
  result=0
  for i in range(0, n):
    if result < sum(m[i]):
      result = sum(m[i])
  forward_diagonal_sum=0
  reverse_diagonal_sum=0
  for j in range(0, n):
    forward_diagonal_sum=+m[j][j]
    reverse_diagonal_sum=+m[n-j-1][j]
  if result < forward_diagonal_sum:
    result = forward_diagonal_sum
  if result < reverse_diagonal_sum:
    result = reverse_diagonal_sum
  for k in range(0, n):
    temp_list=[]
    for l in range(0, n):
      temp_list.append(m[k][l])
    if result < sum(temp_list):
      result = sum(temp_list)
    temp_list=[]
  print(result)


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