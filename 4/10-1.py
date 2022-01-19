import os
import sys
import time
import re
import math
from collections import deque

path="./10/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

# 역수열(그리디)
# 1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 
# 1부터 n까지 각각의 수 앞에 놓여 있는 
# 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다. 
# 예를 들어 다음과 같은 수열의 경우 
#             4  8  6  2  5  1  3  7
# 1앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5. 이렇게 5개이고,
# 2앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,
# 3앞에 놓인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개......
# 따라서 4  8  6  2  5  1  3  7의 역수열은 5 3 4 0 2 1 1 0 이 된다.
# n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 
# 원래의 수열을 출력하는 프로그램을 작성하세요.

# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<100)이 주어지고, 
# 두 번째 줄에는 역수열이 숫자 사이에 한 칸의 공백을 두고 주어진다.

# ▣ 출력설명
# 원래 수열을 출력합니다.

# ▣ 입력예제 1                                   
# 8
# 5 3 4 0 2 1 1 0

# ▣ 출력예제 1
# 4 8 6 2 5 1 3 7


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  list_input = list(map(int, input().split()))
  list_result = [0]*n
  if n ==10:
    print(list_input)
    for i in range(n):
      count=0
      for j in range(n):
        if list_result[j]==0:
          count+=1
        if count == list_input[i]+1:
          list_result[j]=i+1
          break
      print(list_result)




print('실행시간 :', time.time() - start)