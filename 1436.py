
n = int(input())


name = 666
count = 0

while True:
    if count == n:
        print(name-1)
        break
    else:
        check = 0
        for i in str(name):
            if i == "6":
                check += 1
                if check == 3:
                    count += 1
                    continue
                else: pass
            else:
                check = 0
        name += 1





