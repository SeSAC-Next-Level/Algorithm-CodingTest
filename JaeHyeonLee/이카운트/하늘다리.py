# N 개의 산이 나열(리스트)
# 1 ~ N 까지 번호 부여
# i 번의 높이는 Hi

N = int(input())
mountains = list(map(int, input().split()))

l, r = 0, len(mountains) - 1
checker = l + 1