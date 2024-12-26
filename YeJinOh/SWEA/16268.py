# N, M 격자
def solution():
    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]
        # print(board)
        r = c = 0
        # 상하좌우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        # 특정 지점에 도착하면 자기자신 + 상하좌우의 합을 계산
        max_pollen = 0
        for r in range(N):
            for c in range(M):
                # 특정 지점 도착
                tmp = board[r][c]
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M:
                        tmp += board[nr][nc]

                max_pollen = max(tmp, max_pollen)

        print(f"#{tc} {max_pollen}")


solution()
