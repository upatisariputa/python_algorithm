import os
import sys
import time
import re
import math
from collections import deque

path="./8/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


start = time.time()
  
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n=int(input())
  list_text=[]
  list_poem=[]
  for i in range(n):
    list_text.append(input())
  for k in range(n-1):
    list_poem.append(input())
  print(list_text)
  print(list_poem)






  
print('실행시간 :', time.time() - start)