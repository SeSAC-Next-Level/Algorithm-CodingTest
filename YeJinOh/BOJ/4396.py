import sys

input = sys.stdin.readline


def solution():
    n = int(input())

    trap_map = [list(input().rstrip()) for _ in range(n)]
    # print(trap_map)
    status_map = [list(input().rstrip()) for _ in range(n)]
    # print(status_map)

    ans_map = [[0] * n for _ in range(n)]

    # 8방 탐색
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    d = 0

    isBoomb = False
    for r in range(n):
        for c in range(n):
            if status_map[r][c] == "x":
                if trap_map[r][c] == ".":
                    for d in range(8):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < n and trap_map[nr][nc] == "*":
                            ans_map[r][c] += 1
                elif trap_map[r][c] == "*":
                    isBoomb = True
            elif status_map[r][c] == ".":
                ans_map[r][c] = "."

    if isBoomb:
        for r in range(n):
            for c in range(n):
                if trap_map[r][c] == "*":
                    ans_map[r][c] = "*"

    for ans in ans_map:
        print("".join(map(str, ans)))


solution()

# 지뢰가 있는 칸이 열렸다면 -> 지뢰가 있는 모든 칸이 별표여야 한다.
