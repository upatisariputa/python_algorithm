import os
import sys
import time
import re
import math

path="./6/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

# 씨름 선수(그리디)
# 현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, 
# N명의 지원자가 지원을 했습니다. 
# 현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
# 현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
# “다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 
# 무거운 지원자만 뽑기로 했습니다.”
# 만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 
# 존재한다면 A지원자는 탈락입니다.

# ▣ 입력설명
# 첫째 줄에 지원자의 수 N(5<=N<=50)이 주어집니다.
# 두 번째 줄부터 N명의 키와 몸무게 정보가 차례로 주어집니다. 
# 각 선수의 키와 몸무게는 모두 다릅니다.

# ▣ 출력설명
# 첫째 줄에 씨름 선수로 뽑히는 최대 인원을 출력하세요.

# ▣ 입력예제 1                                   
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60

# ▣ 출력예제 1
# 3

# 출력설명
# (183, 65), (180, 70), (170, 72)가 선발됩니다. (181, 60)은 (183, 65) 때문에 탈락하고, (172, 67)은 
# (180, 70) 때문에 탈락합니다.



start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = int(input())
  applicant=[list(map(int, input().split())) for _ in range(n)]
  applicant.sort(key=lambda x: (x[0], x[1]))
  height = 0
  weight = 0
  count = []
  print(applicant)
  for i in range(n):
    for j in range(i+1, n):
      if applicant[j][0] > applicant[i][0] and applicant[j][1] > applicant[i][1]:
        count.append(i)
  temp = set(count)
  print(n-len(temp))


print('실행시간 :', time.time() - start)