# BOJ 17836 공주님을 구해라
from collections import deque

N, M, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
flag  = [[0] * M for _ in range(N)]
start = [0, 0]
queue = deque()
queue.append(start)
check[0][0] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = len(queue)
time = result = 0

flag = 0
while queue:
    now = queue.popleft()
    r = now[0]
    c = now[1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and check[nr][nc] == 0 and MAP[nr][nc] != 1:
            check[nr][nc] = check[r][c] + 1
            queue.append([nr, nc])
            if MAP[nr][nc] == 2:
                pos1 = [nr, nc]
                flag = 1


if flag == 1:
    nr, nc = pos1[0], pos1[1]
    result = check[nr][nc] - 1 + abs(N-1-nr) + abs(M-1-nc)
    if check[N-1][M-1] > 0:
        result = min(result, check[N-1][M-1] - 1)

if result > T or result == 0:
    print('Fail')
else:
    print(result)

