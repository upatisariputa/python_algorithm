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
file_list_out.sort()

# 랜선자르기(결정알고리즘)
# 엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 
# 그러나 K개의 랜선은 길이가 제각각이다. 
# 선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 
# K개의 랜선을 잘라서 만들어야 한다. 
# 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. 
# (이미 자른 랜선은 붙일 수 없다.)편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 
# 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
# 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. 
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 
# 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
# ▣입력설명
# 첫째 줄에는 엘리트학원이 이미 가지고 있는 랜선의 개수 K, 
# 그리고 필요한 랜선의 개수 N이 입력된다. 
# K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 
# 그리고 항상 K ≦ N 이다.   
# 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 2의31승-1
# 이하의 자연수로 주어진다.
# ▣출력설명
# 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
# ▣입력예제 1                                   
# 4 11
# 802
# 743
# 457
# 539
# ▣출력예제 1
# 200
# 예제설명) 802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 
# 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다.

def algorithm(level):
  number_line = 0
  for i in range(n):
    number_line += l[i]//level
  if number_line == m:
    print(level)
  else:
    algorithm(level-1)


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n, m = map(int, input().split())
  l=[int(input()) for _ in range(n)]
  algorithm(sum(l)//m)


print('실행시간 :', time.time() - start)