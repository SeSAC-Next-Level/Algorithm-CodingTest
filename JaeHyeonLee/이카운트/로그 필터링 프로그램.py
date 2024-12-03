# 정리기능
# 특정 시간에 속하는 로그만 출력
# 키워드 대소문자 구별 X


start, end, keyword = input().split()
N = int(input())

logs = {"INFO": [], "WARN": [], "ERROR": []}
for _ in range(N):
    time, log_type, content = input().split(" ", maxsplit=2)

print(logs)
