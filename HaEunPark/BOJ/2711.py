import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    a, word = input().split()
    a = int(a)

    ans = word[:a-1] + word[a:]

    print(ans)