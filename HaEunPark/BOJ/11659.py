import sys
input = sys.stdin.readline

from itertools import accumulate

N, M = map(int, input().split())
nums = list(map(int, input().split()))

acc_nums = [0] + list(accumulate(nums))

for _ in range(M):
    i, j = map(int, input().split())
    tmp = acc_nums[j] - acc_nums[i-1]

    print(tmp)