import os
import sys
import time
import re
import math

path="./10/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 조합  구하기
# 1부터  N까지  번호가  적힌  구슬이  있습니다.  
# 이  중    
# M개를  뽑는  방법의  수를  출력하는  프로그램을  작성하세요.
# ▣입력설명
# 첫  번째  줄에  자연수  N(3<=N<=10)과  M(2<=M<=N)  이  주어집니다.
# ▣출력설명
# 첫  번째  줄에  결과를  출력합니다.  
# 맨  마지막  총  경우의  수를  출력합니다.
# 출력순서는  사전순으로  오름차순으로  출력합니다.
# ▣입력예제  1                                                                     
# 4  2
# ▣출력예제  1
# 1  2
# 1  3
# 1  4
# 2  3
# 2  4
# 3  4
# 6

def Algorithm(level, s):
  if level ==m:
    for i in range(m):
      print(res[i], end = ' ')
    print()
  else:
    for i in range(s, n+1):
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
    # l = list(map(int, input().split()))
    # l=[int(input()) for _ in range(n)]
    # l.reverse()
    # m = int(input())
    if n ==5:
      res = [0]*n
      result = 0
      Algorithm(0, 1)
      print(result)

  print('실행시간 :', time.time() - start)


# def Algorithm(level, s):
#   global result
#   if level == m:
#     # for i in range(m):
#     #   print(res[i], end=' ')
#     # print()
#     result+=1
#   else:
#     for i in range(s, n+1):
#       res[level]=i
#       Algorithm(level+1, i+1)
