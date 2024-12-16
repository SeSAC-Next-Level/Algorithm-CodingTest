import sys
input = sys.stdin.readline

# 퀸의 공격 범위 : 상하좌우 + 대각선

N = int(input())
# 상/하 공격 범위
visited = [False] * N
# 왼쪽 상단 대각선/오른쪽 하단 대각선 공격 범위
visited2 = [False] * (N*2-1)
# 오른쪽 상단 대각선/왼쪽 하단 대각선 공격 범위
visited3 = [False] * (N*2-1)
ans = 0

# depth : 좌/우 공격 범위
def perm(depth):
  global ans
  if depth == N:
    ans += 1
    return
      
  # 탐색
  for x in range(N):
    if visited[x] or visited2[depth - x] or visited3[depth + x]:
      continue
    
    visited[x] = True
    visited2[depth - x] = True
    visited3[depth + x] = True
        
    perm(depth+1)
        
    visited[x] = False
    visited2[depth - x] = False
    visited3[depth + x] = False
      
perm(0)
print(ans)