# 2589 보물섬
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
# 최단거리 중에 최장거리
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[0] * C for _ in range(R)]


def bfs():

    while q:
        global max_dist
        now = q.pop(0)
        dist = now[2]
        max_dist = max(max_dist, dist)
        for i in range(4):
            n_r = now[0] + dr[i]
            n_c = now[1] + dc[i]
            if 0 <= n_r < R and 0 <= n_c < C \
                    and board[n_r][n_c] == 'L' and visited[n_r][n_c] == 0:
                visited[n_r][n_c] = 1
                q.append([n_r, n_c, dist + 1])


max_dist = 0
q = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':
            q.append([i, j, 0])
            visited[i][j] = 1
            bfs()
            visited = [[0] * C for _ in range(R)]

print(max_dist)





# def dfs(now, dist):
#     global max_dist
#     max_dist = max(max_dist, dist)
#
#     for i in range(4):
#         n_r = now[0] + dr[i]
#         n_c = now[1] + dc[i]
#         if 0 <= n_r < R and 0 <= n_c < C \
#                 and board[n_r][n_c] == 'L' and visited[n_r][n_c] == 0:
#             visited[n_r][n_c] = 1
#             dfs([n_r, n_c], dist+1)
#             visited[n_r][n_c] = 0
#
# max_dist = 0
#
# for i in range(R):
#     for j in range(C):
#         if board[i][j] == 'L':
#             visited[i][j] = 1
#             dfs([i, j], 0)
#             visited[i][j] = 0
#
# print(max_dist)