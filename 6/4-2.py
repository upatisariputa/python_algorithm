import os
import sys
import time
import re
import math

path="./4/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 합이  같은  부분집합
# (DFS  :  아마존  인터뷰)
# N개의  원소로  구성된  자연수  집합이  주어지면,  
# 이  집합을  두  개의  부분집합으로  나누었을  때 
# 두  부분집합의  원소의  합이  서로  같은  경우가  존재하면  “YES"를  출력하고,  
# 그렇지  않으면 ”NO"를  출력하는  프로그램을  작성하세요.
# 둘로  나뉘는  두  부분집합은  서로소  집합이며,  
# 두  부분집합을  합하면  입력으로  주어진  원래의 집합이  되어  합니다.
# 예를  들어  {1,  3,  5,  6,  7,  10}이  입력되면  
# {1,  3,  5,  7}  =  {6,  10}  으로  
# 두  부분집합의  합이 16으로  같은  경우가  존재하는  것을  알  수  있다.
# ▣입력설명
# 첫  번째  줄에  자연수  N(1<=N<=10)이  주어집니다.
# 두  번째  줄에  집합의  원소  N개가  주어진다.  
# 각  원소는  중복되지  않는다.
# ▣출력설명
# 첫  번째  줄에  “YES"  또는  ”NO"를  출력한다.
# ▣입력예제  1   
# 6
# 1  3  5  6  7  10                                                               
# ▣출력예제  1
# YES


def Algorithm(level):
  global sum_list
  global yes
  if yes == True:
    return
  if level == n+1:
    one_list = 0
    zero_list = 0
    # print(check)
    for i in range(1, n+1):
      if check[i]==1:
        one_list+=l[i-1]
      if check[i]==0:
        zero_list+=l[i-1]
    if one_list == zero_list:
      print('yes', end='')
      yes = True
      return
    #   break
    #   return True
    # print() 
  else:
    check[level]=1
    Algorithm(level+1)
    check[level]=0
    Algorithm(level+1)



if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    n = int(input())
    # n, m = map(int, input().split())
    l = list(map(int, input().split()))
    # l=[int(input()) for _ in range(n)]
    # print(n,l)
    # if n ==6:
    yes=False
    sum_list = sum(l)
    check=[0]*(n+1)
    Algorithm(1)
    print()
  print('실행시간 :', time.time() - start)




# def Algorithm(n,l):
#   total=sum(l)
#   print(total)
#   def DFS(level, sum_list):
#     if sum_list>total//2:
#       return
#     if level == n:
#       if sum_list == (total-sum_list):
#         print('YES')
#         return
#     else:
#       DFS(level+1, sum_list+l[level])
#       DFS(level+1, sum_list)
#   DFS(0,0)
#   print('NO')
#   return