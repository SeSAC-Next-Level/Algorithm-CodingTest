T = int(input())
# K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N : 0번에서 N까지 정류장
# M : 충전기가 설치된 정류장 개수

# 0 1 2 3 4 5 6 7 8 9
# 3 2 1 0 
# X O X O X O X O X O

for tc in range(1, T+1):
  K, N, M = map(int, input().split())
  charge = list(map(int, input().split()))
  ans = cur = 0
  move = K

  # 버스가 종점에 도착할 때까지
  while cur < N+1:
    # 충전소없이 계속 이동할 경우
    if move < 0:
      ans = 0
      break
    
    # 현재 충전소에 있을 때
    if cur in charge:
      cur_idx = charge.index(cur)
      nxt = cur_idx+1
      # 갈 수 있는 곳이 없을 경우
      if move == 0:
        print(cur, ans)
        ans += 1
        move = K
      # 최대 갈 수 있는 곳에 다음 충전소 없을 경우
      elif nxt < len(charge) and cur+move < charge[nxt]:
        ans += 1
        move = K
      # 마지막 충전소이고 종점이 더 클 경우
      elif cur == charge[-1] and cur+move < N:
        ans += 1
        move = K
      
    cur += 1
    move -= 1
    
  print(f'#{tc} {ans}')