from heapq import heappop, heappush, heapify
import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    heap = list(map(int, input().split()))
    heapify(heap)

    # m번 연산
    for _ in range(m):
        first = heappop(heap)
        second = heappop(heap)
        new = first + second
        heappush(heap, new)
        heappush(heap, new)

    print(sum(heap))


solution()
