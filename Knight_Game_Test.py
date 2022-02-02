def is_valid(matrix, pot_row, pot_col):
    return 0 <= pot_row < len(matrix) and 0 <= pot_col < len(matrix)


def get_kills(matrix, row, col):
    kills = 0
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = col + cols[index]
        if is_valid(matrix, potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == "K":
                kills += 1
    return kills


def position_and_max_kills(matrix):
    max_kills = 0
    killer_position = []
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix)):
            if matrix[row_index][col_index] == "K":
                kills = get_kills(matrix, row_index, col_index)
                if kills > max_kills:
                    max_kills = kills
                    killer_position = [row_index, col_index]
    return max_kills, killer_position


matrix = [list(input()) for _ in range(int(input()))]
remove_count = 0
rows = [-2, -2, 2, 2, 1, 1, -1, -1]
cols = [-1, 1, -1, 1, -2, 2, -2, 2]
while True:
    killings, position = position_and_max_kills(matrix)
    if position:
        matrix[position[0]][position[1]] = "0"
        remove_count += 1
    else:
        break
print(remove_count)