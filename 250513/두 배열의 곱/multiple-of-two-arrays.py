mat1 = [list(map(int, input().split())) for _ in range(3)]
input()  # 빈 줄로 구분
mat2 = [list(map(int, input().split())) for _ in range(3)]

result = [
    [mat1[i][j] * mat2[i][j] for j in range(3)]
    for i in range(3)
]

for row in result:
    print(*row)
