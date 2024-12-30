# region
"""
N * N
숫자가 시계방향
시작은 0, 0



"""
# endregion


def snail(N):
    lst = [([0] * N) for _ in range(N)]
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    r, c = 0, 0
    cnt = 1
    while cnt <= N * N:
        if 0 <= r < N and 0 <= c < N and lst[r][c] == 0:
            lst[r][c] = cnt
            cnt += 1
        else:
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4
        r += dr[d]
        c += dc[d]

    for r in range(N):
        for c in range(N):
            print(lst[r][c], end=" ")
        print()


T = int(input())
for ts in range(1, T + 1):
    print(f"#{ts}")
    N = int(input())
    snail(N)
