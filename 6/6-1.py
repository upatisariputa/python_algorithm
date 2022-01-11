import os
import sys
import time
import re
import math

path="./6/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 중복순열  구하기
# 1부터  N까지  번호가  적힌  구슬이  있습니다.  
# 이  중  중복을  허락하여  M번을  뽑아  일렬로  나열하는  방법을  모두  출력합니다.
# ▣입력설명
# 첫  번째  줄에  자연수  N(3<=N<=10)과  M(2<=M<=N)  이  주어집니다.
# ▣출력설명
# 첫  번째  줄에  결과를  출력합니다.  
# 맨  마지막  총  경우의  수를  출력합니다.
# 출력순서는  사전순으로  오름차순으로  출력합니다.
# ▣입력예제  1                                                                     
# 3  2
# ▣출력예제  1
# 1  1
# 1  2
# 1  3
# 2  1
# 2  2
# 2  3
# 3  1
# 3  2
# 3  3
# 9


def dfs(level):
  if level == m:
    for i in range(m):
      print(list_check[i], end=' ')
    print()
  else:
    for i in range(1, n+1):
      list_check[level] = i
      dfs(level+1)


if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    n, m = map(int, input().split())
    print(n, m)
    list_check=[0]*m
    dfs(0)

  print('실행시간 :', time.time() - start)