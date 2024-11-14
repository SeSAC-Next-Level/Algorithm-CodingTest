# region 함수, LEGB 규칙
"""
1. 함수
  로직을 담아서 반복 사용
  
2. LEGB 규칙
   1) local 영역에서(함수 내부에서) global 영역 변수를 재할당할 수 없다
   2) local 영역에서 global 영역 변수를 참조할 수 있다
   3) 참고할 때에는 LEGB 우선순위로 참조한다
      Local Enclosed Global Built-in
   
   내장함수 이름으로 변수 사용 지양 
  """
""" a = 5
def my_func1():
  # a = 3
  b = 10
  b += a
  return b

print(my_func1())

a = 3 
def my_func2():
  # a += 7 # error
  global a
  a += 7
my_func2()
print(a)


# global
a = 2

def my_func3():
  # enclosed
  a = 3
  def inner_func():
    # local
    nonlocal a # enclosed 사용 시, 프로그래머스에서 사용 됨
    a += 5
    
    
a = [1,2,3,4,5]
def my_func4():
    # a += [6] # error, 새로 할당 X
    a.append(6) #  """

# endregion

# region 재귀 함수 개념

"""

3. 재귀 함수

함수를 선언할 때 그 함수 내부에서 자기 자신을 또 호출하는 함수
자기자신으로 정의되는 함수
반복문을 대체하는 느낌이다
"""
""" def my_func5(depth):
  # 재귀의 종료 조건
  
  # 탐색 로직
  my_func5(depth+1)
  
  
my_func5() """
# endregion

# region 재귀 실습 1


""" # 재귀함수를 이용해서 nums에서 가장 큰 수를 탐색
nums = [-5, 2, 7, -3, 2, 10, 8, 6, 5, -1]

idx = 0
max_num = -float("INF")

def foo1(idx, max_num):
  print(idx, max_num)
  # 종료 조건
  if idx == len(nums):
    return max_num
  
  # 로직
  max_num = max(nums[idx], max_num)
  
  # 반복 및 종료 조건에 따른 결과
  return foo1(idx + 1, max_num)
  
  
  
answer = foo1(idx, max_num)
print(answer) """
# endregion

# region 재귀 예시


def find(depth):
  if depth == 10:
      print("찾았다")
      return 
  print(f"탐색하는 중... 깊이는 {depth}")

  find(depth + 1)

  print(f"올라가는 중... 깊이는 {depth}")


find(0)
# endregion
