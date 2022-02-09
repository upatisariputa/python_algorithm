import os
import sys
import time
import re
import math
from collections import deque

path="./4/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


start = time.time()
  
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  str_calculating=input()
  list_stack=[]
  for x in str_calculating:
    if x.isdecimal():
      list_stack.append(int(x))
    else:
      if x == '+':
        n1=list_stack.pop()
        n2=list_stack.pop()
        list_stack.append(n2+n1)
      elif x == '-':
        n1=list_stack.pop()
        n2=list_stack.pop()
        list_stack.append(n2-n1)
      elif x == '*':
        n1=list_stack.pop()
        n2=list_stack.pop()
        list_stack.append(n2*n1)
      elif x == '/':
        n1=list_stack.pop()
        n2=list_stack.pop()
        list_stack.append(n2/n1)
  print(list_stack)
    
  

  
print('실행시간 :', time.time() - start)
