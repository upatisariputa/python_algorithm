import os
import sys
import time
import re
import math
from collections import deque

path="./7/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


start = time.time()
  
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  str_required = input()
  n=int(input())
  list_subject=[]
  for i in range(n):
    list_subject.append(input())
  for k in list_subject:
    str_temp = deque(str_required)
    for j in k:
      if str_temp[0]==j:
        str_temp.popleft()
      if len(str_temp) == 0:
        print('yes')
        break
    if len(str_temp) != 0:
      print('no')
  print()






  
print('실행시간 :', time.time() - start)