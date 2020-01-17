import sys
import re

com = re.compile('[a-zA-Z]')

story = []
while 1:
    x = sys.stdin.readline().rstrip()
    story.append(x)
    if x == '.':
        break

def vps(line):
    stack = []
    if line[0] == ")" or line[0] == "]":
        # print("1")
        return "no"
    else: pass
    for s in line:
        if bool(com.match(s)) == True:
            pass
        elif s == " " or s == ".":
            pass
        elif s == "(" or s == "[":
            stack.append(s)
            # print(stack)
        elif s == ")" and stack != []:
            if stack[-1] == "(":
                stack.pop()
            else:
                # print("2")
                return "no"
        elif s == "]" and stack != []:
            if stack[-1] == "[":
                stack.pop()
            else:
                # print("3")
                return "no"
        else:
            # print("4")
            return "no"
    if stack == []:
        return "yes"
    else:
        # print("5")
        return "no"

for i in range(len(story)-1):
    result = vps(story[i])
    print(result)

