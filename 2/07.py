# 소수(에라토스테네스 체)
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다. ▣입력설명첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
# ▣출력설명 첫 줄에 소수의 개수를 출력합니다. 
# ▣입력예제 1  
# 20
# ▣출력예제 1
# 8


import os
import sys
import time
path="./7/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def calculate(a):
  # 다시 풀어보기
  # for i in range(i, a+1, i):
  #
  print(a)



start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  a = int(input())
  calculate(a)
print('실행시간 :', time.time() - start)
  


