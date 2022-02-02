size = int(input())
matrix = []
isFound = False
for i in range (size):

    matrix.append(list(input()))


elemen_to_search = input()

for i in range(size):
    for j in range(size):
        if elemen_to_search == matrix[i][j]:
           print(f"({i}, {j})")
           isFound = True
           break

if isFound == False:
    print(f"{elemen_to_search} does not occur in the matrix")
