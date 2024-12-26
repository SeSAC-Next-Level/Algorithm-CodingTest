# 16268 풍선팡 2

T = int(input())

# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
  N, M = map(int, input().split())
  # N 줄에 걸쳐서 받을거니까 (행의 개수!)
  matrix = [list(map(int, input().split())) for _ in range(N)]

  # 정답 초기화
  ans = 0

  # 순회하면서 
  for r in range(N):
    for c in range(M):

    # tmp 초기값  
      tmp = matrix[r][c]

    # r, c에서 델타탐색(4방향)
      for d in range(4):
        nr, nc = r+dr[d], c+dc[d] 
        
        if 0 <= nr < N and 0 <= nc < M: 
          tmp += matrix[nr][nc]
    
        ans = max(tmp, ans)

  # ans 출력
  print(f'#{tc} {ans}')