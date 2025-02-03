T = int(input())

for _ in range(T):
    results = input()

    ans = 0
    score = 0

    for result in results:
        
        if result == "O":
            ans += 1
            score += ans
        elif result == "X":
            ans = 0

    print(score)