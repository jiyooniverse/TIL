# BOJ 7576 토마토
from collections import deque
M, N = map(int, input().split())
# 1: 익은 토마토, 0: 안 익은 토마토, -1: 빈 칸
MAP = [list(map(int, input().split())) for _ in range(N)]
# check = [[0] * M for _ in range(N)]

# 1. 출발점 찾기
# 2. queue 만들고, 시작 위치 넣어주고,
queue = deque()
for row in range(N):
    for col in range(M):
        if MAP[row][col] == 1:
            queue.append([row, col])
            # check[row][col] = 1
        # elif MAP[row][col] == -1:
            # check[row][col] = -1

while queue:
    now = queue.popleft()
    # now = queue.pop(0)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):  # 상하좌우로만 옮겨감
        next_row = now[0] + dr[i]
        next_col = now[1] + dc[i]
        if (0 <= next_row < N and 0 <= next_col < M) and MAP[next_row][next_col] == 0:# and\
                # check[next_row][next_col] == 0:
            MAP[next_row][next_col] = MAP[now[0]][now[1]] + 1
            queue.append([next_row, next_col])

# 3. 다 끝나고 check 배열 검사
result = 0
for r in range(N):
    if result == -1:
        break
    for c in range(M):
        if MAP[r][c] == 0:
            result = -1
            break
        if MAP[r][c] - 1 > result:
            result = MAP[r][c] - 1
print(result)

