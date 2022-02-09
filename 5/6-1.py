import os
import sys
import time
import re
import math
from collections import deque

path="./6/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


start = time.time()
  
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n, m = map(int, input().split())
  list_patient=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
  dq=deque(list_patient)
  count=0
  list_temp=[]
  while True:
    temp=dq.popleft()
    for i in dq:
      if i[1]>temp[1]:
        dq.append(temp)
    count+=1
    if temp[0]==m:
      print(count)
      break



  
print('실행시간 :', time.time() - start)