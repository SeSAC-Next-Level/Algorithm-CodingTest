# 정확한 값을 찾을 수 없음
# 적어도 어쩌구 저쩌구
# 가능한 탐색을 끝까지 지속
# 이분 탐색
# 0 ~ max
# 절반을 짤라서 필요한 나무보다 자른게 많으면 높이 상향
# 너무 적으면 하향
# 반복
# 더이상 탐색할 수 없을 때까지

"""
4 7
20 15 10 17

15

5 20
4 42 40 26 46

36
"""
import sys

input = sys.stdin.readline

# N, M = map(int, input().split())
# trees = list(map(int, input().split()))

# region while ver
""" 
# 초기값 세팅(l, r, c)
l, r = 0, 1_000_000_000
c = (l + r) // 2
# 반복을 하며(l < r)
while l <= r:
    # c를 가지고 가져갈 수 있는 나무 길이를 계산
    length = 0
    for tree in trees:
        if tree > c:
            length += tree - c

    # length = M
    if length == M:
        break

    # length > M
    elif length > M:
        # l값 갱신
        l = c + 1
    # length < M
    elif length < M:
        # r값을 갱신
        r = c - 1

    # 새로운 c를 갱신
    c = (l + r) // 2

print(c)
 """
# endregion

# 높이의 최댓값 구해야함
# 적어도 M미터의 나무를 집에 가져가야함
# 가장 M가 가까운 수를 찾아야함
# 이진탐색

N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 이진 탐색 조건
# 정렬되어 있어야 한다
# l, r을 알아야 함

l, r = 0, 1_000_000_000
c = (l + r) // 2  # 높이

while l <= r:  # 같다면 M과 딱 맞는 지점
    # 나무전체를 높이로 잘랐을때 값으로 M 과 비교
    length = 0
    for tree in trees:
        if tree > c:
            length += tree - c

    # 같으면 높이 리턴
    if length == M:
        break
    # 목표보다 높이를 낮춰서 잘리는 나무가 많아져야 함 // 작으면 r = c -1
    elif length < M:
        r = c - 1
    # 목표보다 길이합이 크면 높이를 높여야 나무가 적게 잘림 // 크면 l = c + 1
    elif length > M:
        l = c + 1
    # 높이 조절
    c = (l + r) // 2
    
print(c)
