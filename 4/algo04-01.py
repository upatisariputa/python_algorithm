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


def calculate (n, m):
  sorted_list = sorted(m)
  list_length = n[0]
  number_to_find = n[1]
  left = 0
  right = list_length

  while left <=right:
    mid = (left+right)//2
    if sorted_list[mid] > number_to_find:
      right = mid +1
    elif sorted_list[mid] <number_to_find:
      left = mid -1
    elif sorted_list[mid]==number_to_find:
      break;
  print(mid+1)
  return mid


  

def algorithm (n, m):
  m.sort()
  lt=0
  rt=n[0]-1
  while lt <=rt:
    mid = (lt+rt)//2
    if m[mid]==n[1]:
      print(mid+1)
      break
    elif m[mid]>n[1]:
      rt=mid-1
    else:
      lt=mid+1  


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = list(map(int, input().split()))
  m = list(map(int, input().split()))
  # m=[list(map(int, input().split())) for _ in range(7)]
  calculate(n, m)
  # algorithm(n, m)


print('실행시간 :', time.time() - start)


# def calculate (n, m):
  # input_length = n[0]
  # target_number = n[1]
  # m.sort()

  # def innerFn (target_number, left_number, right_number, m):
  #   half_number = (left_number + right_number)//2
  #   if target_number < m[half_number]:
  #     right_number=half_number-1
  #     innerFn(target_number, left_number, right_number, m)
  #   elif target_number > m[half_number]:
  #     left_number=half_number+1
  #     innerFn(target_number, left_number, right_number, m)
  #   elif target_number== m[half_number]:
  #     print(half_number+1)
  #     return
  # innerFn(target_number, 0, input_length, m)