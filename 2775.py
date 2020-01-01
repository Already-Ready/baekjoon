

li = [[0]*14 for i in range(15)]

for i in range(1,15):
    li[0][i-1] = i
    li[i][0] = 1

for i in range(1,15):
    for j in range(1,14):
        li[i][j] = li[i-1][j] + li[i][j-1]

n = int(input())

for i in range(n):
    v = int(input())
    p = int(input())

    print(li[v][p-1])
