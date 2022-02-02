from collections import deque

rows, columns = list(map(int, input().split(" ")))
snake = deque(list(input()))
for row in range(rows):
    s = ""
    for column in range(columns):
        piece = snake.popleft()
        s += piece
        snake.append(piece)
    if row % 2 == 0:
        print(s)
    else:
        print(s[::-1])