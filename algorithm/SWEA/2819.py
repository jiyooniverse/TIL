# 2819 격자판 숫자 이어 붙이기

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(now, cnt, path):
    if cnt > 6:
        str_set.add(path)
        return

    r = now[0]
    c = now[1]
    for i in range(4):
        n_r = r + dr[i]
        n_c = c + dc[i]
        if 0 <= n_r < 4 and 0 <= n_c < 4:
            dfs([n_r, n_c], cnt + 1, path + str(MAP[n_r][n_c]))


T = int(input())
for tc in range(T):
    MAP = [list(map(int, input().split())) for _ in range(4)]

    str_set = set()
    for i in range(4):
        for j in range(4):
            dfs([i, j], 1, str(MAP[i][j]))

    print(f'#{tc + 1} {len(str_set)}')