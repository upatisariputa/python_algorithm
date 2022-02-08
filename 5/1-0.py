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
  
for file in file_list_in:
  num, m=map(int, input().split())
  num=list(map(int, str(num)))
  stack=[]
  for x in num:
      while stack and m>0 and stack[-1]<x:
          stack.pop()
          m-=1
      stack.append(x)
  if m!=0:
      stack=stack[:-m]
  res=''.join(map(str, stack))
  print(res)




print('실행시간 :', time.time() - start)