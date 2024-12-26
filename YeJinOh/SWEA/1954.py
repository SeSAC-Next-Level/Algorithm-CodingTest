def solution():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        snails = [[0 for _ in range(N)] for _ in range(N)]
        # print(snails)
        r = c = 0
        # 우하좌상
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        d = 0
        start = 1

        while start <= N * N:
            snails[r][c] = start
            start += 1

            nr, nc = r + dr[d], c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N or snails[nr][nc] != 0:
                d = (d + 1) % 4  # 방향 바꾸기
                nr, nc = r + dr[d], c + dc[d]

            r, c = nr, nc

        print(f"#{tc}")
        for snail in snails:
            print(*snail)


solution()
