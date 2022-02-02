result = 0
rows, cols = [int(x) for x in input().split(", ")]
matrix = []
for i in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)
    result += sum(matrix[i])


print(result)
print(matrix)
