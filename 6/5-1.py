import os
import sys
import time
import re
import math

path="./5/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
# file_list_out.sort()

# 바둑이  승차(DFS)
# 철수는  그의  바둑이들을  데리고  시장에  가려고  한다.  
# 그런데  그의  트럭은  C킬로그램  넘게  태울수가  없다.  
# 철수는  C를  넘지  않으면서  그의  바둑이들을  가장  무겁게  태우고  싶다.
# N마리의  바둑이와  각  바둑이의  무게  W가  주어지면,  
# 철수가  트럭에  태울  수  있는  가장  무거운 무게를  구하는  프로그램을  작성하세요.
# ▣입력설명
# 첫  번째  줄에  자연수  C(1<=C<=100,000,000)와  N(1<=N<=30)이  주어집니다.
# 둘째  줄부터  N마리  바둑이의  무게가  주어진다.
# ▣출력설명
# 첫  번째  줄에  가장  무거운  무게를  출력한다.
# ▣입력예제  1                                                                     
# 259  5
# 81
# 58
# 42
# 33
# 61
# ▣출력예제  1
# 242

def dfs(level):
  global result
  if level == count_dog:
    sum_weight = 0
    for i in range(0, count_dog):
      if list_check_dog[i] == 1:
        sum_weight += list_weight_dog[i]
    if limit_weight-sum_weight>0 and limit_weight-sum_weight < limit_weight-result :
      result = sum_weight
  else:
    list_check_dog[level]=1
    dfs(level+1)
    list_check_dog[level]=0
    dfs(level+1)


if __name__ == "__main__":
  start = time.time()
  for file in file_list_in:
    sys.stdin=open(path + file, 'rt')
    # n = int(input())
    n, m = map(int, input().split())
    # l = list(map(int, input().split()))
    l=[int(input())  for _ in range(m)]
    print(n, m, l)
    count_dog = m
    limit_weight = n
    list_weight_dog = l
    list_check_dog = [0]*(count_dog+1)
    result = 0
    dfs(0)
    print(result)

print('실행시간 :', time.time() - start)
