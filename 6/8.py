import os
import sys
import time
import re
import math

path="./8/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 순열  구하기
# 1부터  N까지  번호가  적힌  구슬이  있습니다.  
# 이  중    M개를  뽑아  일렬로  나열하는  방법을  모두 출력합니다.
# ▣입력설명
# 첫  번째  줄에  자연수  N(3<=N<=10)과  M(2<=M<=N)  이  주어집니다.
# ▣출력설명첫  번째  줄에  결과를  출력합니다.  
# 맨  마지막  총  경우의  수를  출력합니다.
# 출력순서는  사전순으로  오름차순으로  출력합니다.
# ▣입력예제  1                                                                     
# 3  2
# ▣출력예제  1
# 1  2
# 1  3
# 2  1
# 2  3
# 3  1
# 3  2
# 6

def DFS(level):
  global cnt
  if level==m:
    # for i in range(m):
    #   print(res[i], end=" ")
    cnt+=1
  else:
    for i in range(1, n+1):
      if check[i] == 0:
        check[i]=1
        res[level]=i
        DFS(level+1)
        check[i]=0

if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    # s=input().rstrip()
    # n = int(input())
    n, m = map(int, input().split())
    # l = list(map(int, input().split()))
    # l=[int(input()) for _ in range(n)]
    # l.reverse()
    # m = int(input())
    # print(n,m)
    # if n ==6:
    #   Algorithm(n, m)
    # if m==3:
    cnt = 0 
    res = [0]*n
    check=[0]*(n+1)
    DFS(0)
    print(cnt)
  print('실행시간 :', time.time() - start)


# def Inner(level, res, ch, n, m):
#   if level == m:
#     for i in range(m):
#       print(res[i], end=' ')
#     print()
#   else:
#     for i in range(1, n+1):
#       if ch[i] == 0:
#         ch[i] =1
#         res[level]=i
#         Inner(level+1, res, ch, n, m)
#         ch[i]=0
  

# def Algorithm(n, m):
#   res=[0]*n
#   ch = [0]*(n+1)
#   Inner(0 , res, ch, n, m)