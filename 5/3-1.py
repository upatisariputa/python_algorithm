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
  str_calculating=input()
  list_stack=[]
  result=''
  for i in str_calculating:
    if i == '(':
      list_stack.append(i)
    if i == ')':
      result += list_stack.pop()
    if i == '+' or i == '-':
      list_stack.append(i)
    if i == '*' or i == '/':
      list_stack.append(i)
    else:
      result+=i

  
print('실행시간 :', time.time() - start)
