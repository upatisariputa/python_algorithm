import os
import sys
import time
import re
import math

path="./1/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 최대점수 구하기(DFS)
# 이번  정보올림피아드대회에서  좋은  성적을  내기  위하여  
# 현수는  선생님이  주신  N개의  문제를 풀려고  합니다.  
# 각  문제는  그것을  풀었을  때  얻는  점수와  푸는데  
# 걸리는  시간이  주어지게  됩니다.  제한시간  M안에  N개의  문제  중  
# 최대점수를  얻을  수  있도록  해야  합니다.  
# (해당문제는 해당시간이 걸리면 푸는 걸로 간주한다, 
# 한 유형당 한개만 풀 수 있습니다.)
# ▣입력설명
# 첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다. 
# 두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.
# ▣출력설명
# 첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.
# ▣입력예제 1                                   
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4
# ▣출력예제 1
# 41

def Algorithm(level, r, t):
  global time_sum result_sum
  if time_sum > m and result_sum > r:
    return
  else:
    result_sum = r
    check[level]=1
    for i in range(level, n):
      if check[i] == 1:
        Algorithm(level +1, )




if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    # s=input().rstrip()
    # n = int(input())
    n, m = map(int, input().split())
    # l = list(map(int, input().split()))
    # o = int(input())
    # l=[int(input()) for _ in range(n)]
    # l.reverse()
    l =[list(map(int, input().split())) for _ in range(n)]
    # m = int(input())
    # if n == 7:
    # print(l)
    check = [0]*n
    time_sum=0
    result_sum=0
    Algorithm(0,0)
    

  print('실행시간 :', time.time() - start)