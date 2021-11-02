#정다면체
# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 
# 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.
# ▣입력설명 첫 번째 줄에는 자연수 N과 M이 주어집니다. 
# N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
# ▣출력설명첫 번째 줄에 답을 출력합니다.
# ▣입력예제 1 4 6
# ▣출력예제 15 6 7


import os
import sys
import time
path="./2/5/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


def calculate (first_demension, second_demension):
  sum_two_demensinos_list=[]
  max_value=first_demension+second_demension+2
  count_sum_two_demensions_list=[]
  max_count=0
  max_idx_list=[]
  max_num=0
  for i in range(1, first_demension+1):
    for k in range(1, second_demension+1):
      sum_two_demensinos_list.append(i+k)
  for i in range(2, max_value):
    count_sum_two_demensions_list.append(sum_two_demensinos_list.count(i))
  max_num=max(count_sum_two_demensions_list)
  for idx, num in enumerate(count_sum_two_demensions_list):
    if max_num==num:
      max_idx_list.append(idx+2)

  # print(sum_two_demensinos_list)
  # print(count_sum_two_demensions_list)
  print(max_idx_list)
  return True
  

def algorithm (first_demension, second_demension):
  cnt = [0]*(first_demension+second_demension+3)
  max=-2147000000
  for i in range(1, first_demension+1):
    for j in range(1, second_demension+1):
      cnt[i + j]+=1
  for i in range(first_demension+second_demension+1):
    if cnt[i]>max:
      max=cnt[i]
  for i in range(first_demension+second_demension+1):
    if cnt[i]==max:
      print(i, end=' ')
  print('next')

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n, k = map(int, input().split())
  # answer = calculate(n, k)
  answer = algorithm(n, k)
  # print(answer)
print('실행시간 :', time.time() - start)
  


