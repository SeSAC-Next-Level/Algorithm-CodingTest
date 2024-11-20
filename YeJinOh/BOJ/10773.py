import sys

input = sys.stdin.readline


def solution():
    K = int(input())
    stack = []
    for _ in range(K):
        money = int(input())
        stack.append(money) if money else stack.pop()
    print(sum(stack))


solution()
