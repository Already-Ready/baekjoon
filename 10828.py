import sys

n = int(sys.stdin.readline())

stack = []

# n = int(input())

for i in range(n):

    order = sys.stdin.readline().rstrip()
    # print(order)
    if len(order.split()) == 2:
        stack.insert(0,int(order.split()[1]))

    else:
        if order == "pop":
            if stack == []:
                print(-1)
            else:
                print(stack[0])
                stack.pop(0)
        elif order == "size":
            print(len(stack))
        elif order == "empty":
            if stack == []:
                print(1)
            else:
                print(0)
        # top
        else:
            if not stack == []:
                print(stack[0])
            else:
                print(-1)


