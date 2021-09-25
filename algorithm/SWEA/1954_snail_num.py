# 4. 달팽이 숫자
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
T = int(input())

for test_case in range(T):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    i = 0; j = -1
    dir = 0
    for num in range(1, n*n + 1):   # 1 ~ n^2 까지의 숫자가 들어간다.

        # 다음에 어떤 방향으로 움직일 것 인가?
        ni = i + dx[dir]
        nj = j + dy[dir]
        # 숫자가 있거나 범위를 벗어나면 방향을 변경한다.
        if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] != 0:
            dir = (dir + 1) % 4

        i += dx[dir]
        j += dy[dir]
        arr[i][j] = num

    print(f'#{test_case + 1}')
    for x in range(n):
        for y in range(n):
            print(arr[x][y], end=' ')
        print()