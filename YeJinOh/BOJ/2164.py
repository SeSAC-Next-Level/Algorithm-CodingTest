import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N = int(input())

    cards = [num for num in range(1, N + 1)]
    cards = deque(cards)

    while len(cards) > 1:
        # 맨 위 카드 버린다
        cards.popleft()
        cards.append(cards.popleft())

    # 한 장 남은 카드
    print(cards.pop())


solution()
