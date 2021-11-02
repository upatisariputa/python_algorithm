# 카드  역배치(정올  기출)
# 1부터  20까지  숫자가  하나씩  쓰인  20장의  카드가  아래  그림과  같이  오름차순으로  한  줄로  놓여있다.  
# 각  카드의  위치는  카드  위에  적힌  숫자와  같이  1부터  20까지로  나타낸다. 
# 이제  여러분은  다음과  같은  규칙으로  카드의  위치를  바꾼다:  구간  [a,  b]  
# (단,  1  ≤  a  ≤  b  ≤ 20)가  주어지면  위치  a부터  위치  b까지의  카드를  현재의  역순으로  놓는다.
# 예를  들어,  현재  카드가  놓인  순서가  위의  그림과  같고  구간이  [5,  10]으로  주어진다면,  
# 위치 5부터  위치  10까지의  카드  5,  6,  7,  8,  9,  10을  역순으로  하여  
# 10,  9,  8,  7,  6,  5로  놓는다. 이제  전체  카드가  놓인  순서는  아래  그림과  같다.
# 이  상태에서  구간  [9,  13]이  다시  주어진다면,  
# 위치  9부터  위치  13까지의  카드  6,  5,  11,  12, 13을  역순으로  하여  13,  12,  11,  5,  6으로  놓는다.  
# 이제  전체  카드가  놓인  순서는  아래  그림과  같다.
# 오름차순으로  한  줄로  놓여있는  20장의  카드에  대해  10개의  구간이  주어지면,  
# 주어진  구간의 순서대로  위의  규칙에  따라  순서를  뒤집는  작업을  
# 연속해서  처리한  뒤  마지막  카드들의  배치를  구하는  프로그램을  작성하시오.
# ▣입력설명
# 총  10개의  줄에  걸쳐  한  줄에  하나씩  10개의  구간이  주어진다.  
# i번째  줄에는  i번째  구간의  시작  위치  ai와  끝  위치  bi가  차례대로  주어진다.  
# 이때  두  값의  범위는  1  ≤  ai  ≤  bi  ≤  20이다.
# ▣출력설명1부터  20까지  오름차순으로  놓인  카드들에  대해,  
# 입력으로  주어진  10개의  구간  순서대로  뒤집는  작업을  했을  때  
# 마지막  카드들의  배치를  한  줄에  출력한다. 
# ▣입력예제  1                                                                     
# 5  10
# 9  13
# 1  2
# 3  4
# 5  6
# 1  2
# 3  4
# 5  6
# 1  20
# 1  20
# ▣출력예제  1
# 1  2  3  4  10  9  8  7  13  12  11  5  6  14  15  16  17  18  19  20

import os
import sys
import time
import re

path="./3/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()



def calculate (input_list):
  one_to_twenty = list(range(1, 21))
  for i in input_list:
    change_to_number = list(map(int, i))
    reversed_list = list(reversed(one_to_twenty[change_to_number[0]-1:change_to_number[1]]))
    for j in range(change_to_number[0]-1, change_to_number[1]):
      one_to_twenty[j] = reversed_list[j-change_to_number[0]+1]
  return one_to_twenty
    

def algorithm (play_count, input_list):
  print()


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = []
  for i in range(10):
    n.append(input())
  n = list(map(lambda x: x.split(' ') , n))
  answer = calculate(n)
  print(answer)


print('실행시간 :', time.time() - start)
  


