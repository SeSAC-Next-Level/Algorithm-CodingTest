import sys

input = sys.stdin.readline

from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

i = 0
j = n - 1
tmp = cnt = 0

while i < j:

    tmp = nums[i] + nums[j]

    if tmp < x:
        tmp -= nums[i]
        i += 1

    elif tmp > x:
        tmp -= nums[j]
        j -= 1

    elif tmp == x:
        tmp -= nums[i]
        i += 1
        cnt += 1

print(cnt)
