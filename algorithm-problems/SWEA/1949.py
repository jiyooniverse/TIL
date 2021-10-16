# 1949 등산로 조성

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    candi = []
    max_height = -1
    for i in range(N):
        for j in range(N):
            if MAP[i][j] > max_height:
                max_height = MAP[i][j]
                candi = [[i, j]]
            elif MAP[i][j] == max_height:
                candi.append([i, j])

    def dfs(pos, flag):
        global max_count
        if max_count < check[pos[0]][pos[1]]:
            max_count = check[pos[0]][pos[1]]

        for d in range(4):
            nr = dr[d] + pos[0]
            nc = dc[d] + pos[1]

            if 0 <= nr < N and 0 <= nc < N and check[nr][nc] == 0:
                if MAP[pos[0]][pos[1]] > MAP[nr][nc]:
                    check[nr][nc] = check[pos[0]][pos[1]] + 1
                    dfs([nr, nc], flag)
                    check[nr][nc] = 0

                if MAP[pos[0]][pos[1]] <= MAP[nr][nc] and MAP[pos[0]][pos[1]] > MAP[nr][nc] - K and flag == 0:
                    check[nr][nc] = check[pos[0]][pos[1]] + 1
                    tmp = MAP[nr][nc]
                    MAP[nr][nc] = MAP[pos[0]][pos[1]] - 1
                    dfs([nr, nc], 1)
                    MAP[nr][nc] = tmp
                    check[nr][nc] = 0

    check = [[0] * N for _ in range(N)]
    max_count = 0
    for candi_pos in candi:
        # 시작 위치
        _flag = 0
        check[candi_pos[0]][candi_pos[1]] = 1
        dfs(candi_pos, _flag)
        check[candi_pos[0]][candi_pos[1]] = 0

    print(f'#{tc + 1} {max_count}')