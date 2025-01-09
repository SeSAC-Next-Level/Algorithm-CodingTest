# region https://www.acmicpc.net/problem/1929
"""
1 제외
2 포함
2 나눠지면 ㄴㄴ
3 나눠지면 ㄴㄴ

5부터 + 6 증가

5 + i, 5 + 2 + i
소수인지 확인
루트 값까지 포함하여 확인

visited 확인해서 소수가 아닌 수만 확인



소수 판별

2부터 sqrt(num)까지 증가하는 i 가
num을 나눌 수 있으면 소수 아님
"""


# endregion

# region 구현


# i : visited index
# num : num of nums
# def isPrime(num):
#     sqrt_num = int(num ** 0.5) + 1
#     for n in range(2, sqrt_num + 1):
#         if num % n == 0 :
#             return False
#     return True


# M, N = map(int, input().split())


# is_prime = [True for _ in range(N + 1)]
# is_prime[0] = False     # 0 False
# is_prime[1] = False     # 1 False
#                         # 2와 3은 소수


# for num in range(M, N + 1):
#     # 2로 나뉘거나 3으로 나뉘면 소수 아님
#     if num % 2 == 0 or num % 3 == 0 :
#         is_prime[num] = False
#     # 그 외 판별

#     elif is_prime[num]:
#         is_prime[num] = isPrime(num)
#         if num + 2 < num:
#             is_prime[num] = isPrime(num + 2)

# for i in range(M, N + 1):
#     if is_prime[i]:
#         print(i)


# endregion

# print(40 // 6)
# print(40 + (5 - 40 % 6))
# print(list(num for num in range(40, 40 + (5 - 40 % 6) + 1)))

import sys

input = sys.stdin.readline


def isPrime(M, N):
    if N < 2:
        return
    sqrt_num = int(N**0.5) + 1
    for n in range(2, sqrt_num):
        if is_prime[n]:
            for nn in range(n * n , N + 1, n):
                is_prime[nn] = False
    for i in range(M, N + 1):
        if is_prime[i]:
            print(i)


M, N = map(int, input().split())

is_prime = [True for _ in range(N + 1)]
is_prime[0] = False
is_prime[1] = False
isPrime(M, N)


