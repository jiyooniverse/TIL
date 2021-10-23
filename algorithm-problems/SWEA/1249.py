# 1249 보급로 - dfs 시간 초과
# def dfs(now, cnt):
#     global min_cnt
#     row = now[0]
#     col = now[1]
#     if row == N-1 and col == N-1:
#         min_cnt = min(min_cnt, cnt)
#         return
#     if min_cnt <= cnt:
#         return
#
#     for i in range(4):
#         nr = row + dr[i]
#         nc = col + dc[i]
#         if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
#             visited[nr][nc] = 1
#             dfs([nr, nc], cnt+int(board[nr][nc]))
#             visited[nr][nc] = 0
#
# T = int(input())
# for tc in range(T):
#     N = int(input())    # 지도 크기
#     board = [list(input().rstrip()) for _ in range(N)]
#     # [0, 0]에서 시작 [N-1, N-1]에 도착
#     visited = [[0]*N for _ in range(N)]
#
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     min_cnt = 987654321
#     visited[0][0] = 1
#     dfs([0, 0], 0)
#
#     print(f'#{tc + 1} {min_cnt}')


# dijkstra
import heapq

T = int(input())
for tc in range(T):
    N = int(input())    # 지도 크기
    board = [list(map(int, input())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]
    hq = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    heapq.heappush(hq, [0, 0])
    dist[0][0] = 0

    while hq:
        row, col = heapq.heappop(hq)

        if row == N-1 and col == N-1:
            break

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] <= dist[row][col] + board[nr][nc]:
                    continue
                dist[nr][nc] = dist[row][col] + board[nr][nc]
                heapq.heappush(hq, [nr, nc])

    print(f'#{tc + 1} {dist[N-1][N-1]}')
