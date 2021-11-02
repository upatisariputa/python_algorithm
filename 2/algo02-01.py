import os
import sys
import time

path="./2/1/"

# K번째 수
# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
# 각 케이스별
# 첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다. 두 번째 줄에 N개의 숫자가 차례로 주어진다.
# ▣ 출력설명
# 각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.
# ▣ 입력예제 1 2
# 6253 527389 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
# ▣ 출력예제 1 #1 7
# #2 6
# 입력예제1 해설 :
# case 1 : 2 7 3 8의 숫자 중 오름차순 정렬 했을 때 3번째 숫자는 7이다.
# case 2 : 8 16 6 6 17 3 10 11의 숫자 중 오름차순 정렬 했을 때 3번째 숫자는 6이다.

# 첫번째 줄 에 케이스가 주어짐
# 첫번째 숫자는 몇개의 숫자가 있는지
# 두번째, 세번째는 s, e 까지
# 네번째는 그 두번째 세번째 사이에서 몇번째 숫자인가?

file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

out_list=[]

def calculate (first, second):
  answer = second[first[1]-1:first[2]]
  answer = sorted(answer)
  print(answer[first[3]-1])

start = time.time()

def export_input(input_list):
  first_line = [] 
  second_line = []
  cnt = 0
  for i in input_list:
    if cnt != 0 and cnt%2==1:
      first_line = i.split(' ')
    if cnt != 0 and cnt%2==0:
      second_line = i.split(' ')
    if cnt%2==0 and len(first_line)!=0 and len(second_line)!=0:
      first_line = list(map(int, first_line))
      second_line = list(map(int, second_line))
      calculate(first_line, second_line)
    cnt += 1

for file in file_list_in:
  input_list=[]
  n = open('./2/2/' + file)
  m = n.readlines()
  for i in m:
    y = i.strip('\n')
    input_list.append(y)
  export_input(input_list)

print('실행시간 :', time.time() - start)


start1 = time.time()
# 정답에서
# 파일 가져 오는 법
def algorimsm (n, s, e, k, a):
  a = a[s-1: e]
  a.sort()
  print(a[k-1])

for file in file_list_in:
  sys.stdin = open('./2/2/'+file, 'rt')
  T = int(input())
  for t in range(T):
    n, s, e, k = map(int, input().split())
    a= list(map(int, input().split()))
    algorimsm(n, s, e, k, a)

print('실행시간1 :', time.time() - start1)