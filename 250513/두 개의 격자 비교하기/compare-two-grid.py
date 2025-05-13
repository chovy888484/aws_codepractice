n, m = map(int, input().split())

mat1 = [list(map(int, input().split())) for _ in range(n)]
mat2 = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat1[i][j] != mat2[i][j]:
            result[i][j] = 1

for row in result:
    print(*row)
