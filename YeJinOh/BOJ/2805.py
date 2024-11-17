# N : 나무 수, M : 필요한 나무 길이
# 최소 나무길이보다는 커야하니까 주어진 나무길이 사이에서 높이를 설정해야함
def solution():
    N, M = map(int, input().split())
    trees = sorted(list(map(int, input().split())))
    # print(trees)

    l = 0
    r = trees[-1]
    ans = 0  # 최적 절단 높이

    while l <= r:
        c = (l + r) // 2
        total_length = 0

        for tree in trees:
            if tree > c:
                total_length += tree - c

        if total_length >= M:
            ans = c
            l = c + 1
        elif total_length < M:
            r = c - 1
    print(ans)


solution()
