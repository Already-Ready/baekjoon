#import numpy as np

dice = [0,0,0,0,0,0] #위0 아래1 동2 서3 남4 북5 순서로 값

rows, columns, x, y, runs = map(int, input().split())

field = []


# while time == rows*columns:
for row in range(rows):
    li = list(map(int, input().split()))
    field.append(li)

moves = list(map(int, input().split()))

def start(x,y):
    # start_position_x = x
    # start_position_y = y

    # moves = list(map(int, input().split()))
    position_x = x
    position_y = y
    for i in range(len(moves)):
        temp = 0
        if moves[i] == 1:
            if position_y + 1 < columns:
                position_y += 1
                temp = dice[2]
                field_num = field[position_x][position_y]
                if field_num == 0:
                    dice[2] = dice[0]
                    dice[0] = dice[3]
                    dice[3] = dice[1]
                    dice[1] = temp
                    field[position_x][position_y] = temp

                else:
                    dice[2] = dice[0]
                    dice[0] = dice[3]
                    dice[3] = dice[1]
                    dice[1] = field[position_x][position_y]
                    field[position_x][position_y] = 0
            else : continue

        if moves[i] == 2:
            if position_y -1 >= 0:
                position_y -= 1
                temp = dice[3]
                field_num = field[position_x][position_y]

                if field_num == 0:
                    dice[3] = dice[0]
                    dice[0] = dice[2]
                    dice[2] = dice[1]
                    dice[1] = temp
                    field[position_x][position_y] = temp

                else:
                    dice[3] = dice[0]
                    dice[0] = dice[2]
                    dice[2] = dice[1]
                    dice[1] = field[position_x][position_y]
                    field[position_x][position_y] = 0
            else: continue

        if moves[i] == 3:
            if position_x-1 >= 0:
                position_x -= 1
                temp = dice[5]
                field_num = field[position_x][position_y]

                if field_num == 0:
                    dice[5] = dice[0]
                    dice[0] = dice[4]
                    dice[4] = dice[1]
                    dice[1] = temp
                    field[position_x][position_y] = temp

                else:
                    dice[5] = dice[0]
                    dice[0] = dice[4]
                    dice[4] = dice[1]
                    dice[1] = field[position_x][position_y]
                    field[position_x][position_y] = 0
            else: continue

        if moves[i] == 4:
            if position_x+1 < rows:
                position_x += 1
                temp = dice[4]
                field_num = field[position_x][position_y]
                if field_num == 0:
                    dice[4] = dice[0]
                    dice[0] = dice[5]
                    dice[5] = dice[1]
                    dice[1] = temp
                    field[position_x][position_y] = temp

                else:
                    dice[4] = dice[0]
                    dice[0] = dice[5]
                    dice[5] = dice[1]
                    dice[1] = field[position_x][position_y]
                    field[position_x][position_y] = 0
            else: continue

        print(int(dice[0]))


start(x,y)