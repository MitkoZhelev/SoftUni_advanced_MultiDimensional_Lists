temp_sum = 0
all_sum = 0
rows, cols = [int(x) for x in input().split(" ")]
matrix = []
max_start_i,max_start_j = 0,0
for i in range(rows):
    lines = [int(x) for x in input().split(" ")]
    matrix.append(lines)

for i in range(rows - 2):
    for j in range(cols - 2):
        temp_sum = sum([matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
                        matrix[i + 1][j], matrix[i + 1][j + 1],
                        matrix[i + 1][j + 2], matrix[i + 2][j],
                        matrix[i + 2][j + 1], matrix[i + 2][j + 2]])

        if temp_sum > all_sum:
            max_start_j = j
            max_start_i = i
            all_sum = temp_sum

print(f"Sum = {all_sum}")
for i in  range(3):
    for j in range(3):
        print(matrix[max_start_i+i][max_start_j+ j], end = ' ')
    print()