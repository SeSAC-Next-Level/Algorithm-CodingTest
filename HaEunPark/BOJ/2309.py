import sys
input = sys.stdin.readline

dwarfs = list(int(input()) for _ in range(9))
dwarfs.sort()

spy = list()
flag = False

for i in range(8):
    for j in range(1, 9):

        if i == j :
            continue;

        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            spy.append(i)
            spy.append(j)
            flag = True
            break
    
    if flag:
        break

for idx in range(9):
    if idx in spy:
        continue

    print(dwarfs[idx])