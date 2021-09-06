# BOJ 4963 섬의 개수

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 1은 땅, 0은 바다
    MAP = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    queue = []
    cnt = 0
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(h):
        for j in range(w):
            # 땅이고 방문 안 한 곳이면
            if MAP[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                queue.append([i, j])
                visited[i][j] = 1
                while len(queue) != 0:
                    si, sj = queue.pop()
                    for k in range(8):  # 8방향으로 돌면서 방문 안 한 땅인지 확인
                        next_i = si + dx[k]
                        next_j = sj + dy[k]
                        if 0 <= next_i < h and 0 <= next_j < w and MAP[next_i][next_j] == 1 \
                                and visited[next_i][next_j] == 0:
                            queue.append([next_i, next_j])
                            visited[next_i][next_j] = 1

    print(cnt)
