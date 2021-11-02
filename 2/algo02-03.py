# 대표값
# 대표값 N명의 학생의 수학점수가 주어집니다. 
# N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
# 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
# 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
# ▣입력설명첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연수가 주어집니다. 
# 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
# ▣출력설명 첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
# 평균은 소수 첫째 자리에서 반올림합니다.
# ▣입력예제 1  10
# 45 73 66 87 92 67 75 79 75 80
# ▣출력예제 1 74 7
# 예제설명)평균이  74점으로  평균과  가장  가까운  점수는  73(2번),  75(7번),  75(9번)입니다.  
# 여기서  점수가  높은 75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.

import os
import sys
import time
path="./2/4/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


def calculate (length_input, list_input):
  avg = round(sum(list_input, 0)/length_input, 1)
  result = list_input[0]
  minimun_value=0
  avg_minus_minimum_value=0
  result_list = []
  print('평균', avg)
  for i in range(length_input):
    if abs(list_input[i] - avg) < result:
      minimun_value=list_input[i]
  avg_minus_minimum_value=0
  return result

min=2147000000
def algorithm (length_input, list_input):
  ave=int(sum(list_input)/length_input + 0.5)
  for idx, x in enumerate(list_input):
    tmp=abs(x-ave)
    if tmp<min:
      min=tmp
      score=x
      res=idx+1
    elif tmp==min:
      if x>score:
        score=x
        res=idx+1
  print(ave, res)



start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  k = list(map(int, input().split()))
  print(n)
  print(k)
  answer = calculate(n, k)
  # n, k = map(int, input().split())
  # a=sorted(list(map(int, input().split())), reverse=True)
  # answer = calculate(n, k , a)
  # answer = algorithm(n, k, a)
  print(answer)
print('실행시간 :', time.time() - start)
  


