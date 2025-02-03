import sys
input = sys.stdin.readline

from collections import defaultdict

N = int(input())

sales = defaultdict(int)

for _ in range(N):
    sales[input().rstrip()] += 1

sorted_sales = sorted(sales.items(), key=lambda x: (-x[1], x[0]))

print(sorted_sales[0][0])
