# 2105 디저트 카페

# 오른쪽 위, 오른쪽 아래, 왼쪽 아래, 왼쪽 위
dr = [-1, 1, 1, -1]
dc = [1, 1, -1, -1]

def dfs(now, d, d_count, path):
    global max_sum, max_count
    if len(path) > 1 and now == start_pos:
        max_count = max(max_count, len(path) - 1)
        return

    if d_count == 5:
        return
    # 어차피 사각형으로 연결되면 방향 상관 없음
    # 무조건 한방향으로만 찾기

    # 원래 방향으로 가거나
    n_r = now[0] + dr[d]
    n_c = now[1] + dc[d]
    if 0 <= n_r < N and 0 <= n_c < N and \
            (arr[n_r][n_c] not in path or [n_r, n_c] == start_pos):
        dfs([n_r, n_c], d, d_count, path + [arr[n_r][n_c]])

    # 한번 꺽어서 가거나
    if d_count < 4:
        d = (d + 1) % 4
        n_r = now[0] + dr[d]
        n_c = now[1] + dc[d]
        if 0 <= n_r < N and 0 <= n_c < N and \
                (arr[n_r][n_c] not in path or [n_r, n_c] == start_pos):
            dfs([n_r, n_c], d, d_count+1, path + [arr[n_r][n_c]])


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = -1
    max_sum = -1
    for i in range(N):
        for j in range(N):
            # 처음 위치
            start_pos = [i, j]
            # 지금 위치, path에 개수 채우기
            dfs([i, j], 0, 1, [arr[i][j]])


    print(f'#{tc + 1} {max_count}')
