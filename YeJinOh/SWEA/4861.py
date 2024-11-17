
def solution():
    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        # 입력 받기
        board = [list(input().rstrip()) for _ in range(N)]
        # print(board)

        result = None
        for r in range(N):
            for c in range(N - M + 1):
                # 가로 확인
                if board[r][c] == board[r][c + M - 1]:
                    tmp = board[r][c : c + M]
                    # print(tmp)
                    if tmp == tmp[::-1]:
                        result = "".join(tmp)
                        break  # 내부 for문만 종료됨
            if result:
                break

        # 세로 확인
        if not result:
            for c in range(N):
                for r in range(N - M + 1):
                    if board[r][c] == board[r + M - 1][c]:
                        tmp = "".join(
                            board[i][c] for i in range(r, r + M)
                        ) 
                        if tmp == tmp[::-1]:
                            result = tmp
                            break
                if result:
                    break

        print(f"#{tc} {result}")


solution()
