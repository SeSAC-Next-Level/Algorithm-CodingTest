T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    differ = 0

    for i in range(N-1):
        for j in range(1, N):

            if i == j:
                continue

            if abs(nums[i]-nums[j]) > differ:
                differ = abs(nums[i]-nums[j])

    print(f'#{tc} {differ}')