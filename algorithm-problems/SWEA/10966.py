# 10966 물놀이를 가자
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]

    # 'W' 위치 저장
    check = [[-1] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'W':
                q.append((i, j))
                check[i][j] = 0

    while q:
        pos = q.popleft()
        for d in range(4):
            nr = pos[0] + dr[d]
            nc = pos[1] + dc[d]

            if 0 <= nr < N and 0 <= nc < M and check[nr][nc] == -1:
                check[nr][nc] = check[pos[0]][pos[1]] + 1
                q.append((nr, nc))

    total = 0
    for i in check:
        for j in i:
            total += j
    print(f'#{tc + 1} {total}')
