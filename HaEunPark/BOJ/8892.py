import sys
input = sys.stdin.readline

from itertools import permutations

T = int(input())

for _ in range(T):
    k = int(input())
    words = list(input().strip() for _ in range(k))

    perms = list(permutations(words, 2))

    flag = False

    for perm in perms:

        word = perm[0] + perm[1]
        i = 0
        j = len(word) - 1

        while i <= j:

            if word[i] != word[j]:
                flag = False
                break

            i += 1
            j -= 1
            flag = True


        if flag:
            ans = word
            break

    if flag:
        print(ans)
    else: 
        print(0)