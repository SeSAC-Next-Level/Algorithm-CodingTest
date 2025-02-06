T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    tmp = max_num = min_num = sum(nums[:M])
    ans = 0

    for idx in range(N-M):
        # idx+M번째 수까지 더하고, idx번째 수까지 더한 값을 뺀다.
        tmp += nums[idx+M] - nums[idx]
        max_num = max(max_num, tmp)
        min_num = min(min_num, tmp)

        ans = max_num - min_num

    print(f'#{tc} {ans}')