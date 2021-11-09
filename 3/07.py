# 사과나무(다이아몬드)
# 현수의  농장은  N*N  격자판으로  이루어져  있으며,  
# 각  격자안에는  한  그루의  사과나무가  심어저 있다.  
# N의  크기는  항상  홀수이다.  가을이  되어  사과를  수확해야  하는데  
# 현수는  격자판안의  사과를  수확할  때  다이아몬드  모양의  격자판만  수확하고  
# 나머지  격자안의  사과는  새들을  위해서 남겨놓는다.
# 만약  N이  5이면  아래  그림과  같이  진한  부분의  사과를  수확한다.
# 10  13 10  12  15
# 12 39 30 23  11 
# 11 25 50 53 15
# 19 27 29 37  27
# 19  13 30  13  19
# 현수과  수확하는  사과의  총  개수를  출력하세요.
# ▣입력설명
# 첫  줄에  자연수  N(홀수)이  주어진다.(3<=N<=20) 
# 두  번째  줄부터  N줄에  걸쳐  각  줄에  N개의  자연수가  주어진다. 
# 이  자연수는  각  격자안에  있는  사과나무에  열린  사과의  개수이다.
# 각  격자안의  사과의  개수는  100을  넘지  않는다.
# ▣출력설명
# 수확한  사과의  총  개수를  출력합니다.
# ▣입력예제  1                                                                     
# 5
# 10  13  10  12  15
# 12  39  30  23  11
# 11  25  50  53  15
# 19  27  29  37  27
# 19  13  30  13  19
# ▣출력예제  1
# 379


import os
import sys
import time
import re
import math

path="./7/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def calculate(n, m):
  result=0
  half=n//2
  for i in reversed(range(half)):
    result+=sum(m[i][half-i:half+i+1])
  for k in range(half, n):
    result+=sum(m[k][k-half:n-k+half])
  print(result)

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  m = []
  for i in range(n):
    m.append(list(map(int, input().split())))
  calculate(n, m)


print('실행시간 :', time.time() - start)