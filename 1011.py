import math

n =int(input())

for i in range(n):
    x, y = map(int, input().split())
    stand = 0
    if math.sqrt(y-x) - math.floor(math.sqrt(y-x)) < 0.5:
        stand = math.floor(math.sqrt(y-x))
    else: stand = math.ceil(math.sqrt(y-x))

    if y-x > stand**2:
        print(stand*2)
    elif y-x <= stand**2:
        print(stand*2-1)
