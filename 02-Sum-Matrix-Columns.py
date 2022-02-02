

rows,cols = [int(x) for x in input().split(", ")]
matrix = []

for i in range(rows):
    lines = [int(x) for x in input().split(" ")]
    matrix.append(lines)


for i in range (cols):
    sum = 0
    for j in range(rows):
        sum += matrix[j][i]
    print(sum)

