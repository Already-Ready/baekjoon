import itertools

n, m = map(int, input().split())

li = list(map(int, input().split()))

com_li = 0

for i in itertools.combinations(li,3):
    s = sum(i)
    if s > com_li and s <= m:
        com_li = s
    else: pass

print(com_li)



