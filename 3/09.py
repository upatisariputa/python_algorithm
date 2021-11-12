# 봉우리
# 지도  정보가  N*N  격자판에  주어집니다.  
# 각  격자에는  그  지역의  높이가  쓰여있습니다.  
# 각  격자판의  숫자  중  자신의  상하좌우  숫자보다  큰  숫자는  봉우리  지역입니다.  
# 봉우리  지역이  몇  개 있는  지  알아내는  프로그램을  작성하세요. 
# 격자의  가장자리는  0으로  초기화  되었다고  가정한다.만약  N=5  이고,  
# 격자판의  숫자가  다음과  같다면  봉우리의  개수는  10개입니다.
# 0  0  0  0  0  0  0
# 0  5  3  7  2  3  0
# 0  3  7  1  6  1  0
# 0  7  2  5  3  4  0
# 0  4  3  6  4  1  0
# 0  8  7  3  5  2  0
# 0  0  0  0  0  0  0
# ▣입력설명
# 첫  줄에  자연수  N이  주어진다. (1<=N<=50) 
# 두  번째  줄부터  N줄에  걸쳐  각  줄에  N개의  자연수가  주어진다.  
# 각  자연수는  100을  넘지  않는다. 
# ▣출력설명
# 봉우리의  개수를  출력하세요.
# ▣입력예제  1                                                                     
# 5
# 5  3  7  2  3
# 3  7  1  6  1
# 7  2  5  3  4
# 4  3  6  4  1
# 8  7  3  5  2
# ▣출력예제  1
# 10




import os
import sys
import time
import re
import math

path="./9/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def make_list_zero_insert_grid(length_grid, list_grid):
  list_zero_insert_grid=list_grid
  length_grid_insert_zero=length_grid+2
  list_zero=list([0]*length_grid_insert_zero)
  list_zero_insert_grid.insert(0, list_zero)
  list_zero_insert_grid.append(list_zero)
  for i in range(length_grid_insert_zero):
    if(i!= 0 or i==length_grid_insert_zero-1):
      list_zero_insert_grid[i].insert(0, 0)
      list_zero_insert_grid[i].append(0)
  return list_zero_insert_grid

def calculate(length_grid, list_grid):
  result=0
  list_zero_insert_grid = make_list_zero_insert_grid(length_grid, list_grid)
  for i in range(1, length_grid+1):
    for j in range(1, length_grid+1):
      temp_value=list_zero_insert_grid[i][j]
      upper_value=list_zero_insert_grid[i-1][j]
      lower_value=list_zero_insert_grid[i+1][j]
      right_value=list_zero_insert_grid[i][j-1]
      left_value=list_zero_insert_grid[i][j+1]
      if(temp_value > upper_value and temp_value > lower_value and temp_value > right_value and temp_value > left_value):
        result+=1
  print(result)

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  # m = []
  # for i in range(1, n+1):
  #   m.append(list(map(int, input().split())))
  m = [list(map(int, input().split())) for _ in range(n)]
  calculate(n, m)
  # algorithm()


print('실행시간 :', time.time() - start)