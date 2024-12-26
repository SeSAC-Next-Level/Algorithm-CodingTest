from heapq import heappop, heappush

import sys

input = sys.stdin.readline


def solution():
    heap = []

    N = int(input())
    for _ in range(N):
        num = int(input())
        if num:
            heappush(heap, (abs(num), 1 if num > 0 else 0))
        else:
            # 힙 비어있는지 확인
            if not heap:
                print(0)
            else:
                abs_num, sign = heappop(heap)
                result = abs_num if sign > 0 else -abs_num
                print(result)



solution()
