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
# file_list_out.sort()

# 동전교환
# 다음과  같이  여러  단위의  동전들이  주어져  있을때  
# 거스름돈을  가장  적은  수의  동전으로  교환해주려면  
# 어떻게  주면  되는가?  
# 각  단위의  동전은  무한정  쓸  수  있다.
# ▣입력설명
# 첫  번째  줄에는  동전의  종류개수  N(1<=N<=12)이  주어진다.  
# 두  번째  줄에는  N개의  동전의  종류가  주어지고,  
# 그  다음줄에  거슬러  줄  금액  M(1<=M<=500)이  주어진다. 
# 각  동전의  종류는  100원을  넘지  않는다.
# ▣출력설명
# 첫  번째  줄에  거슬러  줄  동전의  최소개수를  출력한다.
# ▣입력예제  1                                                                     
# 3
# 1  2  5
# 15
# ▣출력예제  1
# 3
# 설명 : 5 5 5 동전 3개로 거슬러 줄 수 있다.

def DFS(level, sum_list, stop):
  global res
  if stop == True:
    return
  if sum_list == m and level < res:
    res = level
    DFS(level, sum_list, True)
    # print(res)
    return
  if sum_list > m or level>res:
    return
  else:
    for i in range(n):
      DFS(level+1, sum_list+l[i], False)


if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    # s=input().rstrip()
    n = int(input())
    # n, m = map(int, input().split())
    l = list(map(int, input().split()))
    # l=[int(input()) for _ in range(n)]
    l.reverse()
    m = int(input())
    # print(n,m,l)
    res=2147000000
    # stop =False
    DFS(0,0, False)
    print(res)
  print('실행시간 :', time.time() - start)



# def DFS(level,i,sum_coin):
#   if  sum_coin == m:
#     print(level)
#     return
#   elif sum_coin >m:
#     DFS(level-1,i+1, sum_coin-l[i])
#   else:
#     DFS(level+1,i,sum_coin+l[i])

# def DFS(L, sum_coin):
#     global res
#     if L>=res:
#         return
#     if sum_coin>m:
#         return
#     if sum_coin==m:
#         if L<res:
#             res=L
#     else:
#         for i in range(n):
#             DFS(L+1, sum_coin+l[i])