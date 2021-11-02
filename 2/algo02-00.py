import os
import sys
import time

path="./2/1/"

# K번째 약수
# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
# 6을 예로 들면
# 6 ÷ 1 = 6 … 0
# 6 ÷ 2 = 3 … 0
# 6 ÷ 3 = 2 … 0
# 6 ÷ 4 = 1 … 2
# 6 ÷ 5 = 1 … 1
# 6 ÷ 6 = 1 … 0
# 그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.
# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을
# 작성하시오.
# ▣ 입력설명
# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N
# 이하이다.
# ▣ 출력설명
# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서
# K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.
# ▣ 입력예제 1
# 6 3
# ▣ 출력예제 1
# 3

# n을 1부터 나누어서 0이 되는 것들 중 k 번째 를 꺼낸다. k까지 오지 않았을 경우 -1을 출력

file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

input_list = []
out_list=[]
answer=[]

def calculation (n, k):
  temp_answer = []
  for i in range(1, n+1):
    if n%i==0:
      temp_answer.append(i)
      if len(temp_answer)==k:
        answer.append(i)
        break
  if len(temp_answer) < k:
    answer.append(-1)

def algorimsm (n, k):
  cnt=0
  for i in range(1, n+1):
    if n%1==0:
      cnt+=1
    if cnt==k:
      print(i)
      break
  else:
    print(-1)

start = time.time()

for file in file_list_in:
  sys.stdin=open("./2/1/" + file)
  n, k = map(int, input().split())
  input_list.append((n,k))
  calculation(n, k)

for file in file_list_out:
  sys.stdin=open('./2/1/' + file)
  n = int(input())
  out_list.append(n)
  
print('인풋값', input_list)
print('예상값', out_list)
print('출력값', answer)
print('실행시간', time.time() - start)

# n, k = input()

# n=6
# k=3
# answer=[]

# for i in range(1, n+1):
#   if n%i==0:
#     answer.append(i)
#     if len(answer)==k:
#       print(answer[k-1])
#       break
#   else:
#     print('no')