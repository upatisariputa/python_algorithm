# 격자판  회문수
# 1부터  9까지의  자연수로  채워진  7*7  격자판이  주어지면  
# 격자판  위에서  가로방향  또는 세로방향으로  길이  5자리  회문수가  몇  개  있는지  
# 구하는  프로그램을  작성하세요.
# 회문수란  121과  같이  앞에서부터  읽으나  뒤에서부터  읽으나  같은  수를  말합니다.
# 2 4 1 5 3 2 6 
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8 
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5
# 빨간색처럼  구부러진  경우(87178)는  회문수로  간주하지  않습니다.
# ▣입력설명
# 1부터  9까지의  자연수로  채워진  7*7격자판이  주어집니다.
# ▣출력설명
# 5자리  회문수의  개수를  출력합니다.
# ▣입력예제  1                                                                     
# 2  4  1  5  3  2  6
# 3  5  1  8  7  1  7
# 8  3  2  7  1  3  8
# 6  1  2  3  2  1  1 
# 1  3  1  3  5  3  2
# 1  1  2  5  6  5  2
# 1  2  2  2  2  1  5
# ▣출력예제  1
# 3

import os
import sys
import time
import re
import math

path="./11/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


def calculate (m):
  cnt = 0 
  for i in range(7):
    for j in range(3):
      if m[i][j] == m[i][j+4] and m[i][j+1] == m[i][j+3]:
        cnt += 1
  for i in range(3):
    for k in range(7):
      if m[i][k] == m[i+4][k] and m[i+1][k] == m[i+3][k]:
        cnt +=1
  print(cnt)

def algorithm ():
  print()  


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  m=[list(map(int, input().split())) for _ in range(7)]
  calculate(m)
  # algorithm()


print('실행시간 :', time.time() - start)