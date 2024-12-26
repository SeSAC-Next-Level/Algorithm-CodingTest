# N 영역, M 파리채 크기


def solution():
    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())

        flies = [list(map(int, input().split())) for _ in range(N)]

        max_flies = 0

        # 2중 for문으로 flies를 순회하며
        for r in range(N - M + 1):  # 마지막 미포함이니까 +1
            for c in range(N - M + 1):
                # r, c를 기준으로 잡아
                # 순회
                tmp = 0
                for x in range(r, r + M):
                    for y in range(c, c + M):
                        # 파리 개수 세어주기
                        tmp += flies[x][y]
                max_flies = max(tmp, max_flies)

        print(f"#{tc} {max_flies}")


solution()
