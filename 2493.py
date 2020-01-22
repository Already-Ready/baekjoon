import sys

n = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))

stack = []


for idx,i in enumerate(tower):
    # print(stack)

    while stack:
        if i > stack[-1][1]:
            stack.pop()
        elif i < stack[-1][1]:
            print(stack[-1][0], end=" ")
            stack.append((idx+1,i))
            break


    if not stack:
        stack.append((idx+1,i))
        print(0, end=" ")

    else: continue









