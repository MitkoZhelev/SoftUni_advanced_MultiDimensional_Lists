
size = int(input())

matrix = []

for i in range(size):
    lines = [int(x) for x in input().split(" ")]
    matrix.append(lines)

sum = 0
for i in range(size):
    sum += matrix[i][i]

print(sum)
