# 수들의  합
# N개의  수로  된  수열  A[1],  A[2],  ...,  A[N]  이  있다.  
# 이  수열의  i번째  수부터  j번째  수까지의 합  A[i]+A[i+1]+...+A[j-1]+A[j]가  M이  되는  
# 경우의  수를  구하는  프로그램을  작성하시오.
# ▣입력설명
# 첫째  줄에  N(1≤N≤10,000),  M(1≤M≤300,000,000)이  주어진다.  
# 다음  줄에는  A[1],  A[2],  ..., A[N]이  공백으로  분리되어  주어진다.  
# 각각의  A[x]는  30,000을  넘지  않는  자연수이다.
# ▣출력설명
# 첫째  줄에  경우의  수를  출력한다.
# ▣입력예제  1                                                                     
# 8  3
# 1  2  1  3  1  1  1  2
# ▣출력예제  1
# 5


import os
import sys
import time
import re

path="./5/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def calculate (n, m):
  length_of_m=n[0]
  correct_number=n[1]
  cnt = 0
  for i in range(length_of_m):
    for j in range(i, length_of_m):
      if correct_number == sum(m[i:j]):
        cnt +=1
        break
  print(cnt)
    

def algorithm (b, a):
  n = b[0]
  m = b[1]
  lt=0
  rt=1
  tot=a[0]
  cnt=0
  while True:
    if tot<m:
      if rt<n:
        tot+=a[rt]
        rt+=1
      else:
        break
    elif tot==m:
      cnt+=1
      tot-=a[lt]
      lt+=1
    else:
      tot-=a[lt]
      lt+=1
  print(cnt)


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = list(map(int, input().split()))
  m = list(map(int, input().split()))
  # calculate(n, m)
  algorithm(n,m)


print('실행시간 :', time.time() - start)