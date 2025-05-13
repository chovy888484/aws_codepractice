matrix = [list(map(int, input().split())) for _ in range(3)]

new_matrix = [[num * 3 for num in row] for row in matrix]

for row in new_matrix:
    print(*row)
