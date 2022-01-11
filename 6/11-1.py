import os
import sys
import time
import re
import math

path="./11/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 수들의  조합
# N개의  정수가  주어지면  그  숫자들  중  K개를  뽑는  조합의  합이  
# 임의의  정수  M의  배수인  개수는  몇  개가  있는지  
# 출력하는  프로그램을  작성하세요.
# 예를  들면  5개의  숫자  2  4  5  8  12가  주어지고,  
# 3개를  뽑은  조합의  합이  6의  배수인  조합을 찾으면  
# 4+8+12  2+4+12로  2가지가  있습니다.
# ▣입력설명
# 첫줄에  정수의  개수  N(3<=N<=20)과  임의의  정수  K(2<=K<=N)가  주어지고, 
# 두  번째  줄에는  N개의  정수가  주어진다.
# 세  번째  줄에  M이  주어집니다.
# ▣출력설명총  가지수를  출력합니다.
# ▣입력예제  1                                                                     
# 5  3
# 2  4  5  8  12
# 6
# ▣출력예제  1
# 2


def dfs(level, s):
  global result
  if level == m :
    if sum(res)%number_multiple == 0:
      result +=1
  else:
    for i in range(s, list_count):
      res[level]=list_number[i]
      dfs(level+1, i+1)
        

if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    # s=input().rstrip()
    # n = int(input())
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    o = int(input())
    list_count = n
    count_number = m
    list_number = l
    number_multiple=o
    print(n, m, l, o)
    res = [0]*(m)
    result =0
    dfs(0, 0)
    print(result)
    

  print('실행시간 :', time.time() - start)