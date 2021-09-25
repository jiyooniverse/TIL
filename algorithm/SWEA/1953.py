# 1953 탈주범검거
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

pipe = [[], [1, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 0]]
connect = [1, 0, 3, 2]
T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]
    check = [[0] * M for _ in range(N)]
    q = [[R, C]]
    check[R][C] = 1

    ans = 0
    while q:
        now = q.pop(0)
        ans += 1

        # L시간까지 움직일 수 있음
        if check[now[0]][now[1]] >= L : continue

        for k in range(4):
            nr = now[0] + dr[k]
            nc = now[1] + dc[k]

            if 0 <= nr < N and 0 <= nc < M and check[nr][nc] == 0 and MAP[nr][nc] != 0:
                # 지금 위치 pipe type
                curr_pipe = pipe[MAP[now[0]][now[1]]]
                next_pipe = pipe[MAP[nr][nc]]
                # 움직일 방향으로 파이프가 뚫려 있나? # 다음 방향도
                next_k = connect[k]
                if curr_pipe[k] == 1 and next_pipe[next_k] == 1:
                    check[nr][nc] = check[now[0]][now[1]] + 1
                    q.append([nr, nc])

    print(f'#{tc + 1} {ans}')



