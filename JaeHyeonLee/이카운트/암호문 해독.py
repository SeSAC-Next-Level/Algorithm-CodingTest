# 특정문자 -> 매칭문자(고유함)

# 매칭 이후 또 매칭 문자가 있다면 다시 변환

# 매칭 정보가 없을 때까지

# 무한 반복이면 '?' 출력


crytogram = list(input())
N = int(input())
role = {}
for _ in range(N):
    k, v = input().split()
    role[k] = v


idx = 0

# 인덱스가 배열의 길이 전까지 반복
while idx < len(crytogram):
    cnt = 0
    # 매칭이 된다면
    while role.get(crytogram[idx]) != None:
        # 문자 치환
        word = crytogram[idx]
        crytogram[idx] = role.get(word)
        
        # 중복없는 고유의 치환 문자이므로
        # 변환 과정이 52번 초과 한다면 무한 반복되고 있음
        cnt += 1
        if cnt > 53:
            crytogram[idx] = '?'
            break
    # 치환 종료 후 다음 문자
    idx += 1
print("".join(crytogram))

""" 
print('''
a
52
a Z
b a
c b
d c
e d
f e
g f
h g
i h
j i
k j
l k
m l
n m
o n
p o
q p
r q
s r
t s
u t
v u
w v
x w
y x
z y
A z
B A
C B
D C
E D
F E
G F
H G
I H
J I
K J
L K
M L
N M
O N
P O
Q P
R Q
S R
T S
U T
V U
W V
X W
Y X
Z Y

''')



"""