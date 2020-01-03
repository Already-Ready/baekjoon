import math


runs = int(input())

for run in range(runs):
    x1,y1,r1,x2,y2,r2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    r1 = int(r1)
    x2 = int(x2)
    y2 = int(y2)
    r2 = int(r2)

    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    #print(d)

    if x1 != x2 or y1 != y2:
        # 두점에서 만나는 경우
        if (abs(r1-r2) < d) and (d < abs(r1+r2)):
            print(2)
            #print("case1")
        # 한점에서 만나는데 외접인 경우
        elif r1+r2 == d:
            print(1)
            #print("case2")
        # 한점에서 만나는데 내접인 경우
        elif abs(r1-r2) == d:
            print(1)
            #print("case3")
        # 만나지 않는 경우 - 1. 외부에 있는 경우
        elif r1+r2 < d:
            print(0)
            #print("case4")
        # 만나지 않는 경우 - 2. 내부에 있는 경우
        elif d < abs(r1-r2):
            print(0)
            #print("case5")
    elif x1 == x2 and y1 == y2:
        # 동심원의 경우 - 즉, d=0인 경우 1 : 원안에 원이 쏙 들어간 경우 2 : 원이 겹치는 경우
        if d == 0:
            if r1 == r2: #겹치는 경우
                print(-1)
                #print("case6")
            else :
                print(0) # 원안의 원
                #print("case7")