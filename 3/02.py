# 숫자만  추출
# 문자와  숫자가  섞여있는  문자열이  주어지면  
# 그  중  숫자만  추출하여  그  순서대로  자연수를  만듭니다.  
# 만들어진  자연수와  그  자연수의  약수  개수를  출력합니다.
# 만약  “t0e0a1c2h0er”에서  숫자만  추출하면  0,  0,  1,  2,  0이고  
# 이것을  자연수를  만들면  120이 됩니다.  
# 즉  첫  자리  0은  자연수화  할  때  무시합니다.    
# 출력은  120를  출력하고,  다음  줄에  120의  약수의  개수를  출력하면  됩니다.
# 추출하여  만들어지는  자연수는  100,000,000을  넘지  않습니다.
# ▣입력설명
# 첫  줄에  숫자가  섞인  문자열이  주어집니다. 
# 문자열의  길이는  50을  넘지  않습니다.
# ▣출력설명
# 첫  줄에  자연수를  출력하고,  두  번째  줄에  약수의  개수를  출력합니다.
# ▣입력예제  1                                                                     
# g0en2Ts8eSoft
# ▣출력예제  1
# 28
# 6


import os
import sys
import time
import re

path="./2/"
file_list=os.listdir(path)
file_list_in= [file for file in file_list if file.startswith('in')]
file_list_out= [file for file in file_list if file.startswith('out')]
file_list_in.sort()
file_list_out.sort()

def extract_number(input_str):
  string_in_number=int(''.join(re.findall('\d', input_str)))
  return string_in_number

def count_divisor(number):
  result_count=0
  for i in range(1, number+1):
    if(number%i==0):
      result_count+=1
  return result_count

def calculate(input_list):
  input_str = ''.join(input_list)
  string_in_number = extract_number(input_str)
  count= count_divisor(string_in_number)
  print(count)


start = time.time()
for file in file_list_in:
  sys.stdin=open(path + file, 'rt')
  n = list(input())
  calculate(n)


print('실행시간 :', time.time() - start)
  


