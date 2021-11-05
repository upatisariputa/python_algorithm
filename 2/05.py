# 정다면체
# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 
# 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.
# ▣입력설명 
# 첫 번째 줄에는 자연수 N과 M이 주어집니다. 
# N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
# ▣출력설명
# 첫 번째 줄에 답을 출력합니다.
# ▣입력예제 1 4 6
# ▣출력예제 15 6 7


import os
import sys
import time
path="./5/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

start = time.time()

def calculate(n, m):
    sum_dice_list=[]
    dice_list=[0]*(n+m+1)
    for i in range(1, n+1):
        for k in range(1, m+1):
            sum_dice_list.append(i+k)
    for j in sum_dice_list:
        dice_list[j]=dice_list[j]+1
    max_dice_list=max(dice_list)
    result_list=[]
    for l in range(0, len(dice_list)):
        if(max_dice_list== dice_list[l]):
            result_list.append(l)
    print(result_list)            


for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n, m = map(int, input().split())
  calculate(n, m)



print('실행시간 :', time.time() - start)
  


