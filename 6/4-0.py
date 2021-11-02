# 전역변수와 지역변수

def DFS1():
  cnt=3
  print(cnt)

def DFS2():
  global cnt # global 전역변수
  if cnt == 5:
    print(cnt)


if __name__ == "__main__": # 메인함수 선언, 시작을 의미 해당코드 밑에 main등의 함수를 작성하여 호출
  cnt=5 # 전역변수는 모든 함수가 접근가능
  DFS1()
  DFS2()
  print(cnt)


# 파이썬에서 __name__ 변수는 내부적으로 사용되는 특별한 변수 이름입니다. 
# 위의 예제에서 python taeng.py와 같이 직접 taeng.py 파일을 실행하는 경우에는 
# __name___ 변수에 __main__ 이라는 값이 할당됩니다.

# 다만 마지막에서 살펴본 모듈 불러오기와 같이 import taengModule을 통해서 모듈을 불러와서 사용하는 경우 
# __name__ 변수에는 모듈 이름(여기서는 taengModule)이 저장됩니다.

# 결론적으로 if __name__ == "__main__"와 같이 조건문을 사용하여 
# 터미널에서와 같이 직접 호출되어 사용될 때는 
# 그 자체로 기능을 수행하고, 
# 동시에 다른 모듈에서 필요한 함수 등을 제공할 수 있습니다.