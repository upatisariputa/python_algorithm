import imp
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
# file_list_out.sort()

# 미로의 최단거리 통로(BFS 활용)
# 7*7 격자판 미로를 탈출하는 최단경로의  경로수를  출력하는  프로그램을 작성하세요. 
# 경로수는 출발점에서  도착점까지  가는데  이동한  횟수를  의미한다.  
# 출발점은  격자의  (1, 1)  좌표이고,  탈출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 도로이다.
# 격자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면

# 출발 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 도착

# 위와 같은 경로가 최단 경로이며 경로수는 12이다. 

# ▣ 입력설명
# 7*7 격자판의 정보가 주어집니다.

# ▣ 출력설명
# 첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.

# ▣ 입력예제 1                                   
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0
# ▣ 출력예제 1
# 12

# def dfs(level, x, y):
#   if x == y == 6:
#     print(level)
#   else :
#     if y <= 6:
#       if a[x+1][y]==0 and list_check[x+1][y] != 1:
#         list_check[x+1][y] = 1
#         dfs(level+1, x+1, y)
#       if a[x-1][y]==0 and list_check[x-1][y] != 1:
#         list_check[x-1][y] = 1
#         dfs(level+1, x-1 , y)
#       if a[x][y-1]==0 and list_check[x][y-1] != 1:
#         list_check[x][y-1] = 1
#         dfs(level+1, x, y-1)
#     if x <= 6:
#       if a[x][y+1]==0 and list_check[x][y+1] != 1:
#         list_check[x][y+1] = 1
#         dfs(level+1, x, y+1)
#       if a[x-1][y]==0 and list_check[x-1][y] != 1:
#         list_check[x-1][y] = 1
#         dfs(level+1, x-1, y)
#       if a[x][y-1]==0 and list_check[x][y-1] != 1:
#         list_check[x][y-1] = 1
#         dfs(level+1, x, y-1)
#     else:
#       return


if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    a=[list(map(int, input().split())) for _ in range(7)]
    list_check = [[0]*7 for _ in range(7)]
    list_temp=[]
    result = 0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    que=deque()
    level=0
    que.append((0,0))
    while True:
      if que.popleft()==(0,0):
        print(level)
      size = len(que)
      for i in range(size):
        tmp=que.popleft()
        for j in range(4):
          x=tmp[0]+dx[j]
          y=tmp[1]+dy[j]
          if list_check[x][y] == 0 and a[x][y]==0:
            list_check[x][y]=1
            que.append((x,y))



    # dfs(0, 0, 0)

    

  print('실행시간 :', time.time() - start)