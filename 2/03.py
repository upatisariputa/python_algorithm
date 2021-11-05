# k 번째 큰수
# 현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다.
# 같은 숫자의 카드가 여러장 있을 수 있습니다. 
# 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다.
# 3장을 뽑을 수 있는 모든 경우를 기록합니다. 
# 기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
# 만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 
# K번째 큰 값 은 22입니다.
# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 된다.
# ▣ 출력설명
# 첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.
# ▣ 입력예제 1
# 10 3
# 13 15 34 23 45 65 33 11 26 42
# ▣ 출력예제 1 
# 143


import os
import sys
import time

path="./3/"

file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def algorithm(length_input, count_input, list_input):
    sorted_list=list(reversed(sorted(list_input)))
    print(sorted_list)
    res=set()
    for i in range(length_input):
        for j in range(i+1, length_input):
            for k in range(j+1, length_input):
                res.add(sorted_list[i]+sorted_list[j]+sorted_list[k])    
    sorted_res=list(reversed(sorted(res)))
    print('답', sorted_res[count_input-1])
    
    # de_duplication_list = set(list_input)
    # sorted_list = list(reversed(sorted(de_duplication_list)))
    # print(sorted_list)

    

for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n, k = map(int, input().split())
  a=sorted(list(map(int, input().split())), reverse=True)
  algorithm(n, k, a)
#   print(n, k)
#   print(a)
  


