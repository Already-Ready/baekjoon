import sys

n = int(sys.stdin.readline())


def vps(li):
    stack = []

    if li[0] == ")":
        return "NO"
    else:
        for s in li:
            if s == "(":
                stack.append(s)
            elif s == ")" and stack != []:
                stack.pop()
            else:
                return "NO"

        if stack == []:
            return "YES"
        else: return "NO"

for i in range(n):
    order = list(sys.stdin.readline().rstrip())
    print(vps(order))


