import os
import sys
import time
import re
import math
from collections import deque

path="./9/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


start = time.time()
  
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  str_first=input()
  str_second=input()
  anagram_first=dict()
  anagram_second=dict()
  result='Yes'
  for i in str_first:
    if anagram_first.get(i) == None:
      anagram_first[i]=1
    else:
      anagram_first[i]+=1
  for k in str_second:
    if anagram_second.get(k) == None:
      anagram_second[k]=1
    else:
      anagram_second[k]+=1
  for key, val in anagram_first.items():
    if anagram_first[key] != anagram_second[key]:
      result='No'
      break
  print(result)








  
print('실행시간 :', time.time() - start)