# 스토쿠  검사
# 스도쿠는  매우  간단한  숫자  퍼즐이다.  
# 9×9  크기의  보드가  있을  때,  각  행과  각  열,  
# 그리고  9개의  3×3  크기의  보드에  1부터  9까지의  숫자가  
# 중복  없이  나타나도록  보드를  채우면  된다. 
# 예를  들어  다음을  보자.

# 1 4 3   6 2 8   5 7 9
# 5 7 2   1 3 9   4 6 8
# 9 8 6   7 5 4   2 3 1
# 3 9 1   5 4 2   7 8 6
# 4 6 8   9 1 7   3 5 2
# 7 2 5   8 6 3   9 1 4
# 2 3 7   4 8 1   6 9 5
# 6 1 9   2 7 5   8 4 3
# 8 5 4   3 9 6   1 2 7    

# 위  그림은  스도쿠를  정확하게  푼  경우이다.  
# 각 행에  1부터  9까지의  숫자가  중복  없이  나오고,  
# 각  열에  1부터  9까지의  숫자가  중복  없이  나오고,  
# 각  3×3짜리  사각형(9개이며,  위에서  색깔로  표시되었다)에  
# 1부터  9까지의  숫자가  중복  없이  나오기  때문이다.
# 완성된  9×9  크기의  수도쿠가  주어지면  정확하게  풀었으면  “YES",  
# 잘  못  풀었으면  ”NO"를  출력하는  프로그램을  작성하세요.
# ▣입력설명
# 첫  번째  줄에  완성된  9×9  스도쿠가  주어집니다.
# ▣출력설명
# 첫째  줄에  “YES"  또는  ”NO"를  출력하세요.

# ▣입력예제  1                                                                     
# 1  4  3  6  2  8  5  7  9
# 5  7  2  1  3  9  4  6  8
# 9  8  6  7  5  4  2  3  1
# 3  9  1  5  4  2  7  8  6
# 4  6  8  9  1  7  3  5  2
# 7  2  5  8  6  3  9  1  4
# 2  3  7  4  8  1  6  9  5
# 6  1  9  2  7  5  8  4  3
# 8  5  4  3  9  6  1  2  7

# ▣출력예제  1
# YES



import os
import sys
import time
import re
import math

path="./10/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()


def calculate (m):
  result='YES'
  list_nine=list(range(1, 10))
  for i in range(9):
    list_sorted=sorted(m[i])
    list_vertical=[]*9
    for j in range(9):
      if list_nine[j]!=list_sorted[j]:
        result='NO'
        print(result)
        break;
      # else:
      #   list_vertical.append(m[j][i])
      #   list_sorted_vertical=sorted(list_vertical)
      #   if(list_nine != list_sorted_vertical):
      #     result='NO'
      #     print(result)
      #     break;
  print(result)

def algorithm(m):
  # 가로, 세로, 대각선 각 temp에 넣고 비교
  print(m)

start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  # n = int(input())
  # m = []
  # for i in range(1, n+1):
  #   m.append(list(map(int, input().split())))
  m=[list(map(int, input().split())) for _ in range(9)]
  calculate(m)
  # algorithm()


print('실행시간 :', time.time() - start)