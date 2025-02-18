import sys
input = sys.stdin.readline

n = int(input())

memo = [0, 1]

for _ in range(n-1):
    # 뒤에서 첫번째, 두번째 값을 더해줌
    memo.append(memo[-1] + memo[-2])

print(memo[n])