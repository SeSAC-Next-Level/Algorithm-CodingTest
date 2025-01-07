T = int(input())


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 정답 초기화
    ans = 0
    # 순회하면서
    for r in range(N):
        for c in range(M):
            tmp = matrix[r][c]
            # r, c에서 델타탐색(4방향)
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    tmp += matrix[nr][nc]
    # ans
            ans = max(ans, tmp)
    print(f'#{tc} {ans}')