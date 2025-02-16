import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

i = 0
j = 0
cnt = 0

while True:

    # 오른쪽 포인터가 인덱스 범위를 벗어나면 break
    if j == N+1:
        break

    # i부터 j번째 수까지의 합
    tmp = sum(nums[i:j:1])

    # 합이 M과 같으면,
    if tmp == M:
        # 정답 체크하고, 오른쪽 포인터를 오른쪽으로 이동
        cnt += 1
        j += 1

    # 합이 M보다 작으면,
    elif tmp < M:
        # 오른쪽 포인터를 오른쪽으로 이동
        j += 1

    # 합이 M보다 크면,
    else:
        # 왼쪽 포인터를 오른쪽으로 이동
        i += 1    

print(cnt)