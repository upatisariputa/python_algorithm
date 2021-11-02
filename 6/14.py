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
# file_list_out.sort()

# 인접행렬(가중치  방향그래프)
# 아래  그림과  같은  그래프  정보를  인접행렬로  표현해보세요.
# 251257545234655
# ▣입력설명
# 첫째  줄에는  정점의  수  N(2<=N<=20)와  간선의  수  M가  주어진다.  
# 그  다음부터  M줄에  걸쳐  연결정보와  거리비용이  주어진다.
# ▣출력설명
# 인접행렬을  출력하세요.
# ▣입력예제  1                                                                     
# 6 9
# 1 2 7
# 1 3 4
# 2 1 2
# 2 3 5
# 2 5 5
# 3 4 5
# 4 2 2
# 4 5 5
# 6 4 5 
# ▣출력예제  1
# 0  7  4  0  0  0
# 2  0  5  0  5  0
# 0  0  0  5  0  0
# 0  2  0  0  5  0
# 0  0  0  0  0  0
# 0  0  0  5  0  0




def Algorithm(level, s):
  global result
  if level == m:
    temp =[]
    for i in range(m):
      temp += [l[res[i]]]
      # print(res[i], end=' ')
    if sum(temp)%o == 0:
    # print(temp)
      result+=1
    # print()
  else:
    for i in range(s, n):
      res[level]=i
      Algorithm(level+1, i+1)

        


if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    # s=input().rstrip()
    # n = int(input())
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    o = int(input())
    # l=[int(input()) for _ in range(n)]
    # l.reverse()
    # m = int(input())
    # if n == 7:
    print(n, m, l, o)
    res = [0]*(n+1)
    result =0
    Algorithm(0, 0)
    print(result)
    

  print('실행시간 :', time.time() - start)