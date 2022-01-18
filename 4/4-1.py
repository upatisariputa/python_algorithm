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
file_list_out.sort()

# 마구간 정하기(결정알고리즘)
# N개의 마구간이 수직선상에 있습니다. 
# 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 
# 마구간 간에 좌표가 중복되는 일은 없습니다.
# 현수는 C마리의 말을 가지고 있는데, 
# 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 
# 각 마구간에는 한 마리의 말만 넣을 수 있고, 
# 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다. 
# C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 
# 그 최대값을 출력하는 프로그램을 작성하세요.
# ▣입력설명
# 첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
# 둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.
# ▣출력설명
# 첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.
# ▣입력예제 1                                   
# 5 3
# 1
# 2
# 8
# 4
# 9
# ▣출력예제 1
# 3

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n, m = map(int, input().split())
  l=[int(input()) for _ in range(n)]


print('실행시간 :', time.time() - start)

# 말을 배치하면서 차이를 알아내는게 아니라
# 거리를 줄여가면서 거리를 mid로 놓고
# 차이가 줄어들면 말이 배치가 되는지
# start = time.time()
# for file in file_list_in:
#   sys.stdin=open(path + file, 'rt')
#   n, m = map(int, input().split())
#   l=[int(input()) for _ in range(n)]
#   right = n-1
#   left = 0
#   check = [0]*n
#   check[0]=1
#   check[n-1]=1
#   res = 0
#   count = 0
#   while left <= right:
#     middle = (right+left)//2
#     count+=1
#     max_distance=0
#     for i in range(n):
#       if check[i]==0:
#         left_difference = l[left]-l[i]
#         right_difference = l[i]-l[right]
#         if left_difference > right_difference and max_distance > left_difference:
#           max_distance = left_difference
#           check[i]=1
#         if left_difference < right_difference and max_distance > right_difference:
#           max_distance = right_difference
#           check[i]=1