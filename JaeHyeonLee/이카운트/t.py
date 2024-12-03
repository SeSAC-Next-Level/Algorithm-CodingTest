# 

# 입력 받기
N = int(input())
heights = list(map(int, input().split()))

ans = 0 
stack = [] # 산의 인덱스 저장

# 배열을 역순으로 순회합니다.
for i in range(N-1, -1, -1):
    # 스택이 비어 있지 않고 스택의 맨 위 산의 높이가 현재 산의 높이보다 작으면 스택에서 제거
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()
    # 스택이 비어 있지 않고 스택의 맨 위 산의 높이가 현재 산의 높이와 같다면, 유효한 쌍을 찾은 것이므로 카운트 증가
    if stack and heights[stack[-1]] == heights[i]:
        ans += 1
    # 현재 산의 인덱스를 스택에 추가
    stack.append(i)

# 결과 출력
print(ans)
