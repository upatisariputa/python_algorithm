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
file_list_out.sort()

# 이분검색
# 임의의 N개의 숫자가 입력으로 주어집니다.  
# N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 
# 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요. 
# 단 중복값은 존재하지 않습니다.

# ▣입력설명
# 첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다.
# 두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.
# ▣출력설명
# 첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.
# ▣입력예제 1                                   
# 8 32
# 23 87 65 12 57 32 99 81
# ▣출력예제 1
# 3


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = list(map(int, input().split()))
  m = list(map(int, input().split()))
  m.sort()
  right = 0
  left = n[0]-1
  while m[(left+right)//2] != n[1]:
    middle = (left+right)//2
    if m[middle] == n[1]:
      print(n, m[middle])
      print(middle)
      print()
      break
    elif m[middle] > n[1]:
      left = middle+1
    # elif m[middle] < n[1]:
    else:
      right = middle-1
      
      




print('실행시간 :', time.time() - start)
