import os
import sys
import time
import re
import math
from collections import deque
path="./10/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()


# 미로탐색(DFS)
# 7*7 격자판  미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요.  
# 출발점은 격자의 (1, 1)  좌표이고, 탈출 도착점은 (7, 7)좌표이다. 
# 격자판의  1은 벽이고, 0은 통로이다. 
# 격자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면

# 출발 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 0 0 0 1
# 1 1 0 1 1 0 0
# 1 0 0 0 0 0 도착

# 위의 지도에서 출발점에서 도착점까지 갈 수 있는 방법의 수는 8가지이다.

# ▣ 입력설명
# 7*7 격자판의 정보가 주어집니다.
# ▣ 출력설명
# 첫 번째 줄에 경로의 가지수를 출력한다.

# ▣ 입력예제 1                                   
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 0 0 0 1
# 1 1 0 1 1 0 0
# 1 0 0 0 0 0 0

# ▣ 출력예제 1
# 8

def dfs(x, y):
  global result
  if x==6 and y==6:
    result += 1
  else:
    for i in range(4):
      temp_x=x+dx[i]
      temp_y=y+dy[i]
      if 0<=temp_x<=6 and 0<=temp_y<=6 and board[temp_x][temp_y]==0:
        board[temp_x][temp_y]=1
        dfs(temp_x, temp_y)
        board[temp_x][temp_y]= 0


if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    board=[list(map(int, input().split())) for _ in range(7)]
    result = 0
    board[0][0]=1
    dfs(0, 0)

    print(result)

    

  print('실행시간 :', time.time() - start)