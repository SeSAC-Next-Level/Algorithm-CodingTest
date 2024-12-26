# 순회, 전치, 델타 탐색

matrix = [[3, 7, 9], [4, 2, 6], [8, 1, 5]]

# 1-1. 행 우선 순회,  -> 방향
trails = []

for r in range(3):
    for c in range(3):
        trails.append(matrix[r][c])

print(trails)  # [3, 7, 9, 4, 2, 6, 8, 1, 5]


# 1-2. 행 우선 순회, <- 방향
trails = []

for r in range(3):
    for c in range(2, -1, -1):  # start, end, step
        trails.append(matrix[r][c])

print(trails)  # [5, 1, 8, 5, 1, 8, 5, 1, 8]


# 1-3. 행 우선 순회, 열 지그재그
trails = []

for r in range(3):
    if r % 2 == 0:
        for c in range(3):
            trails.append(matrix[r][c])
    else:
        for c in range(2, -1, -1):
            trails.append(matrix[r][c])

print(trails)  # [3, 7, 9, 6, 2, 4, 8, 1, 5]


# 2-1. 열 우선 순회 ↓
trails = []

for c in range(3):
    for r in range(3):
        trails.append(matrix[r][c])

print(trails)  # [3, 4, 8, 7, 2, 1, 9, 6, 5]

# 2.2. 열 우선 순회, 교차 ↓ ↑ ↓
trails = []

for c in range(3):
    if c % 2 == 0:
        for r in range(3):
            trails.append(matrix[r][c])
    if c % 2 == 1:
        for r in range(2, -1, -1):
            trails.append(matrix[r][c])

print(trails)  # [3, 4, 8, 1, 2, 7, 9, 6, 5]


# 전치 : 행과 열을 뒤집는다.

matrix = [[3, 7, 9], [4, 2, 6], [8, 1, 5]]



# 1. for문을 이용한 전치
for r in range(3):
    for c in range(3):
        if r > c:  # r < c나 둘 중 하나, 둘 다 수행시 원상복귀
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

for i in range(3):
    print(matrix[i])
# [3, 4, 8]
# [7, 2, 1]
# [9, 6, 5]

# 2. zip 함수를 이용한 전치

matrix = [[3, 7, 9], [4, 2, 6], [8, 1, 5]]

# zip 활용 

zipped_matrix = list(zip(*matrix))
print(zipped_matrix) # [(3, 4, 8), (7, 2, 1), (9, 6, 5)]

#  원소를 리스트로 사용하고 싶다면 형변환
transposed_matrix = list(map(list, zip(*matrix)))
print(transposed_matrix) # [[3, 4, 8], [7, 2, 1], [9, 6, 5]]



# 델타 탐색

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

#ex. M[1][1]에서 4방향 탐색

r = c =1

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#4방향 탐색
for d in range(4):
  nr = r + dr[d]
  nc = c + dc[d]
  print(M[nr][nc], end=' ') # 2 8 4 6
  

#ex. M[2][2]에서 4방향 탐색

r = c = 2

for d in range(4):
  nr = r + dr[d]
  nc = c + dc[d]
  
  if 0 <= nr < 3 and 0 <= nc < 3: #인덱스 유효성 검사
    print(M[nr][nc], end=' ') # 6 8
    r, c = nr, nc #이동