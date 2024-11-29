# region 
'''
가중치가 들어간 인접행렬
문제에 주어진 입력값이 구조화 되어 있으므로
문제만 풀면됨

마지막에서 출발지로 가는 경로 + 1

0에서 출발하는 순환 경로 모두 탐색
순환이기 때문에 중복됨
'''

# endregion

# region 풀이

N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]

def perm(depth):
  # 마지막 도시에 도착하면(depth == N)
    # 마지막 - 출발 가는 비용을 더해주고
    # 정답 갱신 하고 리턴
  
  # 갈 수 있는 곳을 탐색하여
    # 방문한적 없고, 0이 아니라면
      # 방문 체크하고
      # 방문(재귀)
      
      # 방문 체크 해제
      pass
visited = [0] * N

perm(0)

# endregion