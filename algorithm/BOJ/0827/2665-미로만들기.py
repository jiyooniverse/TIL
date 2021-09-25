# BOJ 2665 미로 만들기
# 검은색 몇개 흰색으로 바꿔서 통과하면 도착할 수 있는가
from collections import deque
import sys

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
check = [[0] * N for _ in range(N)]
black = [[0] * N for _ in range(N)]
# (0,0)이 시작 위치
queue = deque()
queue.append([0, 0])
check[0][0] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
min_cnt = N * N
while queue:
    now = queue.popleft()
    r = now[0]
    c = now[1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if check[nr][nc] == 0:
                check[nr][nc] = 1
                if MAP[nr][nc] == 1:    # 흰색
                    check[nr][nc] = 1
                    black[nr][nc] = black[r][c]
                else:   # 검은색
                    check[nr][nc] = 1
                    black[nr][nc] = black[r][c] + 1
                queue.append([nr, nc])

            else:   # 방문한 곳이면 black 개수 비교해서 더 작으면 업데이트
                if MAP[nr][nc] == 1:    # 흰색
                    if black[nr][nc] > black[r][c]:
                        black[nr][nc] = black[r][c]
                        queue.append([nr, nc])
                else:   # 검은색
                    if black[nr][nc] > black[r][c] + 1:
                        black[nr][nc] = black[r][c] + 1
                        queue.append([nr, nc])

            # if nr == (N - 1) and nc == (N - 1):
            #     if black[nr][nc] < min_cnt:
            #         min_cnt = black[nr][nc]

print(black[N - 1][N - 1])
