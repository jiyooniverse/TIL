# BOJ 2178 미로 탐색
N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
# 1. queue 생성 후 초기 위치 추가, 방문 표시
queue = []
check[0][0] = 1
queue.append([0, 0])

while queue:
    # 2-1. deque
    now = queue.pop(0)
    # 2-2. 인접 노드 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        nr = now[0] + dr[i]
        nc = now[1] + dc[i]
        if 0 <= nr < N and 0 <= nc < M and MAP[nr][nc] == 1 and check[nr][nc] == 0:
            check[nr][nc] = check[now[0]][now[1]] + 1
            queue.append([nr, nc])

# 3. 탐색 완료 후
print(check[N-1][M-1])