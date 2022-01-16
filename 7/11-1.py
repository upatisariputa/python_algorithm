import os
import sys
import time
import re
import math
from collections import deque
from xmlrpc.client import boolean
path="./11/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()


# 등산경로(DFS)
# 등산을  매우  좋아하는  철수는  마을에  있는  뒷산에  등산경로를  만들  계획을  세우고  있습니다. 
# 마을  뒷산의  형태를  나타낸  지도는  N*N  구역으로  나뉘어져  있으며,  
# 각  구역에는  높이가  함께 나타나 있습니다. 
# N=5이면 아래와 같이 표현됩니다.
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100
# 어떤  구역에서  다른  구역으로  등산을  할  때는  
# 그  구역의  위,  아래,  왼쪽,  오른쪽  중  더  높은 
# 구역으로만  이동할  수  있도록  등산로를  설계하려고  합니다.  
# 등산로의  출발지는  전체  영역에서 가장 낮은 곳이고, 목적지는 가장 높은 곳입니다. 
# 출발지와 목적지는 유일합니다. 
# 지도가  주어지면  출발지에서  도착지로  갈  수  있는    
# 등산  경로가  몇  가지  인지  구하는  프로그램을 작성하세요.

# ▣ 입력설명
# 첫 번째 줄에 N(5<=N<=13)주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.

# ▣ 출력설명
# 등산경로의 가지수를 출력한다.

# ▣ 입력예제 1                                   
# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100

# ▣ 출력예제 1
# 5

def dfs(x, y):
  global result
  if x == point_max[0] and y == point_max[1]:
    result += 1
  else:
    for i in range(4):
      temp_x=x+dx[i]
      temp_y=y+dx[i]
      if  0 <= temp_x < n and 0<= temp_y < n and board[x][y] < board[temp_x][temp_y] and board_check[temp_x][temp_y] ==0:
        board_check[temp_x][temp_y]=1
        dfs(temp_x, temp_y)
        board_check[temp_x][temp_y]=0

if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    n=int(input())
    board=[list(map(int, input().split())) for _ in range(n)]
    board_check=[[0]*n for _ in range(n)]
    result = 0
    number_min=21400000
    number_max=0
    point_min=[0, 0]
    point_max=[0, 0]
    for i in range(0, n):
      for j in range(0, n):
        if board[i][j] < number_min:
          number_min=board[i][j]
          point_min[0] = i 
          point_min[1] = j
        if board[i][j] > number_max:
          number_max=board[i][j]
          point_max[0]=i
          point_max[1]=j
    board_check[point_min[0]][point_max[1]]=1
    dfs(point_min[0], point_min[1])
    print(result)

    

  print('실행시간 :', time.time() - start)