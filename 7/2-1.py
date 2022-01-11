import os
import sys
import time
import re
import math

path="./2/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 휴가(삼성 SW역량평가 기출문제 : DFS활용)
# 카운셀러로 일하고 있는 현수는  오늘부터 N+1일째 되는 날 휴가를 가기  위해서,  남은  N일  동
# 안 최대한 많은 상담을 해서 휴가비를 넉넉히 만들어 휴가를 떠나려 한다.
# 현수가 다니는 회사에 하루에 하나씩 서로 다른 사람의 상담이 예약되어 있다.
# 각각의 상담은 상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P로 이
# 루어져 있다.
# 만약 N = 7이고, 아래와 같이 예약이 잡혔있다면
#    1일 | 2일 | 3일 | 4일 | 5일 | 6일 | 7일
#  T  4  |  2  |  3  |  3  |  2  |  2  | 1
#  P  20 |  10 |  15 |  20 |  30 |  20 | 10
# 1일에 잡혀있는 상담은 총 4일이 걸리며, 상담했을 때 받을 수 있는 금액은 20이다. 만약 1일
# 에 예약된 상담을 하면 4일까지는 상담을 할 수가 없다.
# 하나의  상담이  하루를  넘어가는  경우가  많기  때문에  현수는  예약된  모든  상담을  혼자  할  수 
# 없어 최대 이익이 나는 상담 스케쥴을 짜기로 했다.
# 휴가를  떠나기  전에  할  수  있는  상담의  최대  이익은  1일,  5일,  7일에  있는  상담을  하는  것이
# 며, 이때의 이익은 20+30+10=60이다.
# 현수가 휴가를 가기 위해 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
# ▣ 입력설명
# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
# 둘째 줄부터 1일부터 N일까지 순서대로 주어진다. (1 ≤ T ≤ 7, 1 ≤ P ≤ 100)
# ▣ 출력설명
# 첫째 줄에 현수가 얻을 수 있는 최대 이익을 출력한다.
# ▣ 입력예제 1                                   
# 7
# 4 20 
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10
# ▣ 출력예제 1
# 60


# def dfs(sum_time, sum_point):
#   global result
#   if sum_time >= n-1:
#     if result < sum_point:
#       result = sum_point
#   else:
#     dfs(list_time[sum_time]+sum_time, sum_point+list_point[list_time[sum_time]])


# if __name__ == "__main__":
#   start = time.time()
#   for file in file_list_in:
#     sys.stdin=open(path + file, 'rt')
#     input=sys.stdin.readline
#     n = int(input())
#     list_time=list()
#     list_point=list()
#     for i in range(n):
#       a, b = map(int, input().split())
#       list_time.append(a)
#       list_point.append(b)
#     result = 0
#     for i in range(0, n):
#       dfs(i, list_point[i])
#     print(result)
    

#   print('실행시간 :', time.time() - start)

def dfs(sum_time, sum_point):
  global result
  if sum_time == n:
    if result < sum_point:
      result = sum_point
  else:
    if sum_time+list_time[sum_time] <= n:
      dfs(list_time[sum_time]+sum_time, sum_point+list_point[sum_time])
    dfs(sum_time+1, sum_point)


if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    n = int(input())
    list_time=list()
    list_point=list()
    for i in range(n):
      a, b = map(int, input().split())
      list_time.append(a)
      list_point.append(b)
    result = 0
    dfs(0, 0)
    print(result)
    

  print('실행시간 :', time.time() - start)