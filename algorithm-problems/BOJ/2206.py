# 2206 벽 부수고 이동하기
import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# [0, 0]에서 [R-1, C-1]까지 가는 최단 거리,
# dfs - 벽하나 부시는 모든 경우
# bfs - 최단 거리

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[[0] * C for _ in range(R)] for _ in range(2)]
def bfs():
    # q = [[0, 0, 1]]
    q = deque()
    q.append([0, 0, 0]) # y, x, 벽 부신적 있는 지
    visited[0][0][0] = 1

    global min_dist
    while q:
        now = q.popleft()

        if now[0] == R - 1 and now[1] == C - 1:
            if min_dist < 0 or min_dist > visited[now[2]][R - 1][C - 1]:
                min_dist = visited[now[2]][R - 1][C - 1]

        for i in range(4):
            n_r = now[0] + dr[i]
            n_c = now[1] + dc[i]

            if 0 <= n_r < R and 0 <= n_c < C and visited[now[2]][n_r][n_c] == 0:
                if board[n_r][n_c] == '0':
                    q.append([n_r, n_c, now[2]])
                    visited[now[2]][n_r][n_c] = visited[now[2]][now[0]][now[1]] + 1

                elif board[n_r][n_c] == '1' and now[2] == 0:
                    visited[1][n_r][n_c] = visited[now[2]][now[0]][now[1]] + 1
                    q.append([n_r, n_c, 1])



min_dist = -1
bfs()
print(min_dist)
