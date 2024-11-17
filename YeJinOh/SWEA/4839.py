def solution():
    T = int(input())

    for tc in range(1, T + 1):

        P, Pa, Pb = map(int, input().split())
        cnt_a = findTargetPage(P, Pa)
        cnt_b = findTargetPage(P, Pb)

        print(f"#{tc} A") if cnt_a < cnt_b else print(f"#{tc} B") if cnt_a > cnt_b else print(f"#{tc} 0")
        

def findTargetPage(Page, target):
    # 초기값
    l = 1
    r = Page
    cnt = 0

    while l <= r:
        c = int((l + r) // 2)
        cnt += 1

        if c == target:
            return cnt
       
        elif c < target:
            l = c

        elif c > target:
            r = c

    return -1  

solution()
