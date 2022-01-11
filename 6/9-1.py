import os
import sys
import time
import re
import math

path="./9/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 수열  추측하기
# 가장  윗줄에  1부터  N까지의  숫자가  한  개씩  적혀  있다.  
# 그리고  둘째  줄부터  차례대로  파스칼의  삼각형처럼  위의  두개를  더한  값이 
#  저장되게  된다.  
# 예를  들어  N이  4  이고  가장  윗  줄에  3 1  2  4  가  있다고  했을  때,  
# 다음과  같은  삼각형이  그려진다.
# 3  1  2  4
# 4  3  6
# 7  9
# 16
# 과 가장 밑에 있는 숫자가 주어져 있을 때 
# 가장 윗줄에 있는 숫자를 구하는 프로그램을 작성하시오.  
# 단,  답이  여러가지가  나오는  경우에는  사전순으로  
# 가장  앞에  오는  것을  출력하여야  한다.
# ▣입력설명
# 첫째  줄에  두개의  정수  N(1≤N≤10)과  F가  주어진다.  
# N은  가장  윗줄에  있는  숫자의  개수를  의미하며  
# F는  가장  밑에  줄에  있는  수로  1,000,000  이하이다.
# ▣출력설명
# 첫째 줄에 삼각형에서 가장 위에 들어갈 N개의 숫자를 빈 칸을 사이에 두고 출력한다. 
# 답이 존재하지  않는  경우는  입력으로  주어지지  않는다.
# ▣입력예제  1                                                                     
# 4  16
# ▣출력예제  1
# 3  1  2  4

if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    input=sys.stdin.readline
    # s=input().rstrip()
    # n = int(input())
    n, m = map(int, input().split())
    # l = list(map(int, input().split()))
    # l=[int(input()) for _ in range(n)]
    # l.reverse()
    # m = int(input())

  print('실행시간 :', time.time() - start)
