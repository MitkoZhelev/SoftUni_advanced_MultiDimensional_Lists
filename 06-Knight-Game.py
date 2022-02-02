def input_to_Board():
    matrix = []
    board_size = int(input())
    for i in range(board_size):
        matrix.append(list(input()))
    return matrix


def isValid(matrix, potential_row, potential_col):
    if 0 < potential_row < len(matrix) and 0 <= potential_col < len(matrix):
        return True


def knight_attack(matrix, row, col):
    kills = 0
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = col + cols[index]
        if isValid(matrix, potential_row, potential_col):
            potential_pos = matrix[potential_row][potential_col]
            if potential_pos == "K":
                kills += 1
    return kills


def knights_attacking_eachother(matrix):
    max_kills = 0
    killer_pos = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "K":
                kills = knight_attack(matrix, row, col)
                if kills > max_kills:
                    max_kills = kills
                    killer_pos = [row, col]

    return max_kills, killer_pos


matrix = input_to_Board()
remove_count = 0
rows = [-2, -2, 2, 2, 1, 1, -1, -1]
cols = [-1, 1, -1, 1, -2, 2, -2, 2]
while True:
    killings, position = knights_attacking_eachother(matrix)
    if position:
        matrix[position[0]][position[1]] = "0"
        remove_count += 1
    else:
        break
print(remove_count)
