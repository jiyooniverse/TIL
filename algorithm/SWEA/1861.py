# 1861 정사각형 방
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(now, cnt):
    global local_cnt
    if cnt > local_cnt:
        local_cnt = cnt

    r = now[0]
    c = now[1]
    for i in range(4):
        n_r = r + dr[i]
        n_c = c + dc[i]
        if 0 <= n_r < N and 0 <= n_c < N and \
                MAP[n_r][n_c] == MAP[r][c] + 1:
            dfs([n_r, n_c], cnt+1)


T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            # 처음 출발
            local_cnt = 0
            dfs([i, j], 1)
            if local_cnt >= max_cnt:
                # 같은 값중에선 작은 값 선택
                if local_cnt == max_cnt:
                    if pos > MAP[i][j]:
                        pos = MAP[i][j]
                else:
                    pos = MAP[i][j]
                max_cnt = local_cnt


    print(f'#{tc + 1} {pos} {max_cnt}')