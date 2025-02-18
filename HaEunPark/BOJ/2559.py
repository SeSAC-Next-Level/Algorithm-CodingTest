import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperature = list(map(int, input().split()))

tmp = max_temperature = sum(temperature[:K])

for idx in range(N-K):
    tmp += temperature[idx+K] - temperature[idx]

    max_temperature = max(tmp, max_temperature)

print(max_temperature)