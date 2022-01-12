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

# 동전 바꿔주기(DFS)
# 명보네 동네 가게의 현금 출납기에는 k가지 동전이 각각 n1, n2, ... , nk개 씩 들어있다.
# 가게  주인은  명보에게  T원의  지폐를  동전으로  바꿔  주려고한다.  
# 이때,  동전  교환  방법은  여러가지가  있을  수  있다.
# 예를  들어,  10원  짜리,  5원  짜리,  1원  짜리  동전이  각각2개,  3개,  5개씩 있을 때, 
# 20원 짜리 지폐를 다음과 같은4가지 방법으로 교환할 수 있다.m m
# 20 = 10×2
# 20 = 10×1+5×2
# 20 = 10×1+5×1+1×5
# 20 = 5×3+1×5
# 입력으로  지폐의  금액  T,  동전의  가지수  k,  각  동전  하나의금액  pi와  개수  ni가  주어질  때
# (i=1,2,...,k) 
# 지폐를 동전으로 교환하는 방법의 가지 수를 계산하는 프로그램을 작성하시오. 
# 방법의 수는 231을 초과하지않는 것으로 가정한다. 

# ▣ 입력설명
# 첫째 줄에는지폐의 금액 T(0<T≤10,000), 둘째 줄에는 동전의 가지 수k(0<k≤10), 셋째 줄부터 
# 마지막 줄까지는 각 줄에 동전의금액 pi(0<pi≤T)와 개수 ni(0<ni≤10)가 주어진다. pi와 ni 사이
# 에는 빈 칸이 하나씩 있다.

# ▣ 출력설명
# 첫  번째  줄에  동전  교환  방법의  가지  수를  출력한다.
# (교환할  수  없는  경우는  존재하지  않는다.)

# ▣ 입력예제 1                                   
# 20
# 3
# 5 3
# 10 2
# 1 5
# ▣ 출력예제 1
# 4


# def dfs(level, sum_money):
#   global result
#   if sum_money > money:
#     return
#   if level==number_coin:
#     print(result)
#   if sum_money == money:
#     result+=1
#   else:
#     for i in range(0, list_count_coin[level]+1):
#       # if level != 0 and sum_money != 0:
#       dfs(level+1, sum_money+list_money_coin[level]*i)
#     # dfs(level+1, sum_money)

# def dfs(level, count_coin, sum_money):
#   global result
#   if sum_money == money:
#     result+=1
#   else:
#     if list_count_coin[level] <= count_coin:
#       dfs(level, count_coin+1, sum_money+list_money_coin[level])
#     dfs(level+1, 0, sum_money)
    



if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    money = int(input())
    number_coin = int(input())
    list_money_coin=list()
    list_count_coin=list()
    for i in range(number_coin):
      a, b = map(int, input().split())
      list_money_coin.append(a)
      list_count_coin.append(b)
    result = 0
    if money== 19:
      dfs(0, 0)
    # print(result)
    

  print('실행시간 :', time.time() - start)