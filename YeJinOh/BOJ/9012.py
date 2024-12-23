import sys

input = sys.stdin.readline


def solution():
    T = int(input())

    for _ in range(T):
        stack = []
        parenthesis = input().rstrip()

        for paren in parenthesis:
            # ( 면 stack에 넣는다
            if paren == "(":
                stack.append(paren)
            elif stack:  # ) and stack에 뭔가 있다면
                stack.pop()
            else:  # ) and stack이 비었다면
                print("NO")
                break
        # for - else구문 (for문을 다 돌았는데도, 결론이 안났다면)
        else:
            print("NO") if stack else print("YES")


solution()
