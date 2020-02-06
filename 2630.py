import sys

n = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


white = 0
blue = 0

def div(x, y, k):
    global white, blue
    temp = 0

    for i in range(x, x + k):
        for j in range(y, y + k):
            if board[i][j]:
                temp += 1

    # 사각형 하나를 순회했을때 사각형이 전부 0이라면 --> 흰색 사각형 발견
    if not temp:
        white += 1
    # 사각형 하나를 순회했을때 사각형이 전부 1이라면 --> 1인 보드의 개수가 n의 제곱 개수만큼 있다는 뜻이므로 파란색 사각형 발견
    elif temp == k**2:
        blue += 1
    # 만약 전부 흰색도 전부 파란색도 아닌 섞인 사각형을 순회했다면? --> 사각형을 4개로 쪼개서 다시 순회한다.
    else:
        # 사각형을 4개로 나누었을 때
        # 왼쪽 위 사각형의 왼쪽 위 모서리 좌표로 div 다시 순회
        div(x, y, k // 2)
        # 오른쪽 위 사각형의 왼쪽 위 모서리 좌표로 div 다시 순회
        div(x, y + k // 2, k // 2)
        # 왼쪽 아래 사각형의 왼쪽 위 모서리 좌표로 div 다시 순회
        div(x + k // 2, y, k // 2)
        # 오른쪽 아래 사각형의 왼쪽 위 모서뢰 좌표로 div 다시 순회
        div(x + k // 2, y + k // 2, k // 2)


div(0,0,n)
print(white)
print(blue)






