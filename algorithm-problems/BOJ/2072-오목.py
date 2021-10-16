# BOJ 2072 오목
n = int(input())
MAP = [[0] * 20 for _ in range(20)] # 1 ~ 19 번까지 사용
res = -1
for i in range(1, n+1):
    # 홀수번 흑, 짝수번 백
    row, col = map(int, input().split())
    MAP[row][col] = i % 2 + 1   # 홀수번 2, 짝수번 1
    # 현위치로부터 가로/ 세로/ 대각선1/ 대각선2 검사
    queue = []
    check = [0] * 20
    queue.append([row, col])
    color = MAP[row][col]
    check[col] = 1
    cnt = 0
    while len(queue) != 0:
        sr, sc = queue.pop(0)
        cnt += 1
        n_c1 = sc + 1
        n_c2 = sc - 1
        if 0 < n_c1 < 20 and check[n_c1] == 0 and MAP[sr][n_c1] == color:
            queue.append([sr, n_c1])
            check[n_c1] = 1
        if 0 < n_c2 < 20 and check[n_c2] == 0 and MAP[sr][n_c2] == color:
            queue.append([sr, n_c2])
            check[n_c2] = 1
    # 가로방향 확인
    if cnt == 5:
        res = i
        break

    queue = []
    check = [0] * 20
    queue.append([row, col])
    check[row] = 1
    cnt = 0
    while len(queue) != 0:
        sr, sc = queue.pop(0)
        cnt += 1
        n_r1 = sr + 1
        n_r2 = sr - 1
        if 0 < n_r1 < 20 and check[n_r1] == 0 and MAP[n_r1][sc] == color:
            queue.append([n_r1, sc])
            check[n_r1] = 1
        if 0 < n_r2 < 20 and check[n_r2] == 0 and MAP[n_r2][sc] == color:
            queue.append([n_r2, sc])
            check[n_r2] = 1
    # 세로 방향 확인
    if cnt == 5:
        res = i
        break

    queue = []
    check2 = [[0] * 20 for _ in range(20)]
    queue.append([row, col])
    check2[row][col] = 1
    cnt = 0
    while len(queue) != 0:
        sr, sc = queue.pop(0)
        cnt += 1
        n_r1, n_c1 = sr + 1, sc + 1
        n_r2, n_c2 = sr - 1, sc - 1
        if 0 < n_r1 < 20 and 0 < n_c1 < 20 and check2[n_r1][n_c1] == 0 and MAP[n_r1][n_c1] == color:
            queue.append([n_r1, n_c1])
            check2[n_r1][n_c1] = 1
        if 0 < n_r2 < 20 and 0 < n_c2 < 20 and check2[n_r2][n_c2] == 0 and MAP[n_r2][n_c2] == color:
            queue.append([n_r2, n_c2])
            check2[n_r2][n_c2] = 1
    # 우하향 방향 확인
    if cnt == 5:
        res = i
        break

    queue = []
    check2 = [[0] * 20 for _ in range(20)]
    queue.append([row, col])
    check2[row][col] = 1
    cnt = 0
    while len(queue) != 0:
        sr, sc = queue.pop(0)
        cnt += 1
        n_r1, n_c1 = sr - 1, sc + 1
        n_r2, n_c2 = sr + 1, sc - 1
        if 0 < n_r1 < 20 and 0 < n_c1 < 20 and check2[n_r1][n_c1] == 0 and MAP[n_r1][n_c1] == color:
            queue.append([n_r1, n_c1])
            check2[n_r1][n_c1] = 1
        if 0 < n_r2 < 20 and 0 < n_c2 < 20 and check2[n_r2][n_c2] == 0 and MAP[n_r2][n_c2] == color:
            queue.append([n_r2, n_c2])
            check2[n_r2][n_c2] = 1
    # 우상향 방향 확인
    if cnt == 5:
        res = i
        break

print(res)

