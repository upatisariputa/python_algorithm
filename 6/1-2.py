import os
import sys
import time
import re
import math

path="./1/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

# 재귀함수 이용 이진수 출력


def Algorithm(n):
  if n == 0:
    return
  else:
    Algorithm(n//2) 
    print(n%2, end=' ')




start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  # n, m = map(int, input().split())
  # l = list(map(int, input().split()))
  # l=[int(input()) for _ in range(n)]
  
  Algorithm(n)
  print()


print('실행시간 :', time.time() - start)


