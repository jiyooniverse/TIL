# 1861 정사각형 방
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    arr = [0] * (N * N + 1)

    for r in range(N):
        for c in range(N):
            for d in range(4):
                n_r = r + dr[d]
                n_c = c + dc[d]
                if 0 <= n_r < N and 0 <= n_c < N and \
                        MAP[n_r][n_c] == MAP[r][c] + 1:
                    # 연결 되어있다.(지금 내 뒤로 숫자 하나 더 가능)
                    arr[MAP[r][c]] = 1
                    break
    max_dist = 0
    dist = 0
    for n in range(N*N, 0, -1):
        if arr[n] == 1:
            dist += 1
            if dist >= max_dist:
                max_dist = dist
                max_pos = n
        else:
            dist = 0

    print(f'#{tc + 1} {max_pos} {max_dist + 1}')



