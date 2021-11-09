# 주사위 게임
# 1에서 부터 6까지의 눈을 가진 
# 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
# 규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.  
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된다. 
# 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다. 
# 3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 
# 600원을 상금으로 받게 된다.
# N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 
# 상금을 출력하는 프로그램을 작성하시오
# ▣입력설명
# 첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 
# 그 다음 줄부터 N개의 줄에 사람들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 
# 각각 주어진다. 
# ▣출력설명
# 첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.
# ▣입력예제 1 
# 3
# 3 3 6
# 2 2 2
# 6 2 5
# ▣출력예제 1
# 12000


import os
import sys
import time
path="./9/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

# def calculate(input_list):
#   result_list=[]
#   for i in input_list:
#     deleted_duplicate=set(i)
#     if(len(deleted_duplicate)==1):
#       result_list.append(i[0]*1000+10000)
#     if(len(deleted_duplicate)==2):
#       result_list.append()
#     if(len(deleted_duplicate)==3):
#       result_list.append(max(i)*100)

def algorithm(n, input_list):
  money=0
  res=0
  for i in input_list:
    i.sort()
    a,b,c=map(int, i)
    if(a==b and b==c):
      money=10000+(a*1000);
    elif(a==b or a==c):
      money=1000+(a*100)
    elif(b==c):
      money=1000+(b*100)
    else:
      money=c*100
    if money > res:
      res=money
  print(res)

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  a = []
  for i in range(n):
    tmp=list(map(int, input().split()))
    a.append(tmp)
  algorithm(n, a)

  

print('실행시간 :', time.time() - start)
  
