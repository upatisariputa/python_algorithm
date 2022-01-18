import os
import sys
import time
import re
import math
from collections import deque
path="./13/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()


# 섬나라 아일랜드(BFS 활용)
# 섬나라 아일랜드의  지도가  격자판의  정보로  주어집니다.  
# 각 섬은 1로 표시되어  상하좌우와  대각선으로  연결되어  있으며,  
# 0은  바다입니다.  
# 섬나라  아일랜드에  몇  개의  섬이  있는지  구하는 프로그램을 작성하세요.
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0
# 만약 위와 같다면 

# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다.
# 두 번째 줄부터 격자판 정보가 주어진다.

# ▣ 출력설명
# 첫 번째 줄에 섬의 개수를 출력한다.

# ▣ 입력예제 1                                   
# 7
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0

# ▣ 출력예제 1
# 5

if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    dx=[-1, -1, 0, 1, 1, 1, 0, -1]
    dy=[0, -1, -1, -1, 0, 1, 1, 1]
    n=int(input())
    board=[list(map(int, input().split())) for _ in range(n)]
    result=[]
    cnt=0
    que = deque()
    for i in range(n):
      for j in range(n):
        if board[i][j]==1:
          board[i][j]=0
          que.append((i,j))
          while que:
            tmp=que.popleft()
            for k in range(8):
              x=tmp[0]+dx[k]
              y=tmp[1]+dy[k]
              if x<0 or x>=n or y<0 or y >=n or board[x][y]==0:
                continue
              board[x][y]=0
              que.append((x, y))
              cnt+=1
          result.append(cnt)
    print(result)
    

  print('실행시간 :', time.time() - start)