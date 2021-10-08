# 17144 미세먼지
R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
MAP_copy = [[0] * C for _ in range(R)]
air_pos = []
dust_pos = [[]]
for i in range(R):
    for j in range(C):
        if MAP[i][j] == -1:
            air_pos.append(i)
        # elif MAP[i][j] != 0:
        #     dust_pos.append([i, j])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(now):
    r = now[0]
    c = now[1]
    now_dust = MAP[r][c] // 5
    for d in range(4):
        n_r = r + dr[d]
        n_c = c + dc[d]

        if 0 <= n_r < R and 0 <= n_c < C and MAP[n_r][n_c] != -1:
            MAP[r][c] -= now_dust
            MAP_copy[n_r][n_c] += now_dust


time = 0
while time < T:
    dust_pos = []
    for i in range(R):
        for j in range(C):
            if j == 0 and i in air_pos:
                MAP[i][j] = -1
            elif MAP[i][j] != 0:
                dust_pos.append([i, j])

    # 미세 먼지 확산
    for dust in dust_pos:
        bfs(dust)
    # 미세먼지 더해주기
    for i in range(R):
        for j in range(C):
            MAP[i][j] += MAP_copy[i][j]
            MAP_copy[i][j] = 0


    # 공기청정기 작동 - 공기청정기로 들어가는 것부터 한 칸씩 이동
    # 1. 공기청정기 있는 열
    for i in range(air_pos[0] - 1, -1, -1):
        MAP[i + 1][0] += MAP[i][0]
        MAP[i][0] = 0
    for i in range(air_pos[1] + 1, R):
        MAP[i - 1][0] += MAP[i][0]
        MAP[i][0] = 0

    # 2. 맨 위, 아래
    for j in range(1, C):
        MAP[0][j - 1] += MAP[0][j]
        MAP[0][j] = 0

        MAP[R - 1][j - 1] += MAP[R - 1][j]
        MAP[R - 1][j] = 0

    # 3. 마지막 열
    for i in range(1, air_pos[0] + 1):
        MAP[i - 1][C - 1] += MAP[i][C - 1]
        MAP[i][C - 1] = 0
    for i in range(R - 2, air_pos[1] - 1, -1):
        MAP[i + 1][C - 1] += MAP[i][C - 1]
        MAP[i][C - 1] = 0

    # 4. 공기청정기 있는 행
    for j in range(C - 2, 0, -1):
        MAP[air_pos[0]][j + 1] += MAP[air_pos[0]][j]
        MAP[air_pos[0]][j] = 0

        MAP[air_pos[1]][j + 1] += MAP[air_pos[1]][j]
        MAP[air_pos[1]][j] = 0

    time += 1

# 다 끝나고 난 뒤 전체 먼지 양 구하기
total = 0
for i in range(R):
    for j in range(C):
        if j == 0 and i in air_pos:
            continue
        elif MAP[i][j] != 0:
            total += MAP[i][j]


print(total)