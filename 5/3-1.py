import os
import sys
import time
import re
import math
from collections import deque

path="./3/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


start = time.time()
  

for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  s=input()
  count=0
  list_stack=[]
  for i in range(len(s)):
    if s[i]=='(':
      list_stack.append(s[i])
    else:
      list_stack.pop()
      if s[i-1] == '(':
        count+=len(list_stack)
      else:
        count+=1
  print(count)
  
print('실행시간 :', time.time() - start)
