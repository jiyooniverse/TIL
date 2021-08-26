# BOJ 18405 경쟁적 전염
N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())     # s초 후에 x, y에 있는 바이러스

queue = [[] for _ in range(K)]  #
result = MAP[X - 1][Y - 1]
# 초기 바이러스 위치
for r in range(N):
    for c in range(N):
        if MAP[r][c] == 0:
            continue
        queue[MAP[r][c] - 1].append([r, c])

cnt = len(queue)
time = 0
while queue and result == 0 and S != time:   # 낮은 바이러스부터 전염된다. S초 동안만
    # 낮은 바이러스가 담긴 queue부터 먼저
    q = queue.pop(0)
    q2 = []    # 새로 담아줄 queue
    cnt -= 1
    while q:    # q라는 queue에서 bfs 실행
        now = q.pop(0)
        if now[0] == X - 1 and now[1] == Y - 1:
            result = MAP[now[0]][now[1]]
            break
        # now의 상하좌우에 now virus 전염
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < N and MAP[nr][nc] == 0:
                MAP[nr][nc] = MAP[now[0]][now[1]]
                q2.append([nr, nc])
    if len(q2) > 0:
        queue.append(q2) # i-virus가 전염된 후 업데이트된 q를 전체 queue에 넣어준다.
    # 한 차례 돌았다.
    if cnt == 0:
        time += 1
        cnt = len(queue)

print(MAP[X - 1][Y - 1])






