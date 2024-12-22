from heapq import heappop, heappush

import sys

input = sys.stdin.readline


def solution():
    heap = []

    N = int(input())
    for _ in range(N):
        num = int(input())
        if num:
            heappush(heap, (abs(num), num))
        else:
            # 힙 비어있는지 확인
            if not heap:
                print(0)
            else:
                abs_num, real_num = heappop(heap)
                print(real_num)


solution()
