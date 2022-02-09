import os
import sys
import time
import re
import math
from collections import deque

path="./5/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


start = time.time()
  
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n, m = map(int, input().split())
  q=list(range(1, n+1))
  dq=deque(q)
  print(dq)
  while dq:
    for _ in range(m-1):
      cur=dq.popleft()
      dq.append(cur)
    dq.popleft()
    if len(dq)==1:
      print(dq[0])
      dq.popleft()
  
print('실행시간 :', time.time() - start)