import os
import sys
import time
import re
import math
from collections import deque

path="./1/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


start = time.time()

def dfs(int_target):
  global count
  if len(list_new) != 0 and list_new[-1] < int_target and count > 0:
    count -= 1
    list_new.pop()
    dfs(int_target)
  else:
    list_new.append(int_target)
  

for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n, m = map(int, input().split())
  list_number = list(map(int, str(n)))
  list_new = []
  count = m
  for i in list_number:
    dfs(i)
  if count > 0:
    list_new = list_new[0:-count]
  print(list_new)




print('실행시간 :', time.time() - start)