import os
import sys
import time
import re
import math

path="./3/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 부분집합  구하기(DFS)
# 자연수  N이  주어지면  1부터  N까지의  
# 원소를  갖는  집합의  부분집합을  모두  출력하는  프로그램을  작성하세요. 
# ▣입력설명
# 첫  번째  줄에  자연수  N(1<=N<=10)이  주어집니다.
# ▣출력설명
# 첫  번째  줄부터  각  줄에  하나씩  부분집합을  아래와  출력예제와  같은  순서로  출력한다. 
# 단  공집합은  출력하지  않습니다.
# ▣입력예제  1                                                                     
# 3
# ▣출력예제  1
# 1  2  3
# 1  2
# 1  3
# 1
# 2  3
# 2
# 3

# 전위 순회 방식

def calculate(n):
  check=[0]*(n+1)
  def dfs(level):
    if n+1==level:
      for i in range(1, n+1):
        if check[i]==1:
          print(i, end='')
      print()
    else:
      check[level]=1
      dfs(level+1)
      check[level]=0
      dfs(level+1)
  dfs(1)

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  # n, m = map(int, input().split())
  # l = list(map(int, input().split()))
  # l=[int(input()) for _ in range(n)]
  # print(n,l)
  calculate(n)


print('실행시간 :', time.time() - start)
