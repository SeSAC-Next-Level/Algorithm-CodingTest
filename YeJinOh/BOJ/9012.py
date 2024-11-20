import sys

input = sys.stdin.readline


def solution():
    T = int(input())

    for _ in range(T):
        stack = []
        parenthesis = input().rstrip()

        for paren in parenthesis:
            if paren == "(":
                stack.append(paren)
            else:
                if stack:
                    stack.pop()
                else:
                    print("NO")
                    break  # 해당 반복문 종료
        else:
            if stack:
                print("NO")
            else:
                print("YES")


solution()
