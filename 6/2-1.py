import os
import sys
import time
import re
import math

# path="./2/"
# file_list=os.listdir(path)
# file_list_in= [file for file in file_list if file.startswith('in')]
# file_list_out= [file for file in file_list if file.startswith('out')]
# file_list_in.sort()
# file_list_out.sort()

# 이진트리 순회
# 깊이우선탐색(DFS) - tree
#    1
#  2  3
# 4 5 6 7


# 전위 순회 방식
# 함수 본연의 작업을 실행후 노드로 뻗어나가면 전위순회
def Pre_DFS (v):
  if v>7:
    return
  else:
    print(v, end=" ")
    Pre_DFS(v*2) # 왼쪽 자식 노드
    Pre_DFS(v*2+1) # 오른쪽 자식 노드
# [1,2,4,5,3,6,7]

# 중위 순회
def IT_DFS (v):
  if v>7:
    return
  else:
    IT_DFS(v*2) # 왼쪽 자식 노드
    print(v, end=" ")
    IT_DFS(v*2+1) # 오른쪽 자식 노드
# [4,2,5,1,6,3,7]

# 후위 순회
# 병합정렬 시
def Post_DFS(v):
  if v>7:
    return
  else:
    Post_DFS(v*2) # 왼쪽 자식 노드
    Post_DFS(v*2+1) # 오른쪽 자식 노드
    print(v, end=" ")
# [4,5,2,6,7,3,1]

def Algorithm():
  Pre_DFS(1)
  print(' ')
  IT_DFS(1)
  print(' ')
  Post_DFS(1)
  print(' ')


start = time.time()
# for file in file_list_in:
#   sys.stdin=open(path + file, 'rt')
  # n, m = map(int, input().split())
  # l = list(map(int, input().split()))
  # l=[int(input()) for _ in range(n)]
Algorithm()


print('실행시간 :', time.time() - start)