n = int(input())

for i in range(1, n + 1):  # i: 현재 행 번호 (1부터 n까지)
    for j in range(n):     # j: 현재 열 인덱스 (0부터 n-1까지)
        if j % 2 == 0:      # 짝수 열일 경우
            print(i, end="")         # 행 번호 i 출력
        else:               # 홀수 열일 경우
            print(n + 1 - i, end="") # (n+1 - i) 출력
    print()  # 줄바꿈
