# 5656 벽돌 깨기
import copy
from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(p, cnt):
    global min_ans
    if cnt == N:
        ans = 0
        for ic in range(R):
            for jc in range(C):
                if map_copy[ic][jc] != 0:
                    ans += 1
        if ans < min_ans:
            min_ans = ans

        return

    #
    q = deque()
    for i in range(R):
        if map_copy[i][p[cnt]] != 0:
            q.append([map_copy[i][p[cnt]], i, p[cnt]])
            map_copy[i][p[cnt]] = 0
            break

    while q:
        b = q.popleft()   # 지금 깰 벽돌
        r = b[1]
        c = b[2]
        num = b[0]  # 깰 벽돌 수
        for d in range(4):
            for ii in range(1, num):
                n_r = r + dr[d] * ii
                n_c = c + dc[d] * ii
                if 0 <= n_r < R and 0 <= n_c < C and map_copy[n_r][n_c] != 0:
                    q.append([map_copy[n_r][n_c], n_r, n_c])
                    map_copy[n_r][n_c] = 0

    # 다 깨고 나면 벽돌 아래로 정리
    for j2 in range(C):
        for i2 in range(R-1, 0, -1):
            if map_copy[i2][j2] == 0:
                ii = i2 - 1
                while ii > 0 and map_copy[ii][j2] == 0:
                    ii -= 1
                map_copy[i2][j2] = map_copy[ii][j2]
                map_copy[ii][j2] = 0
                if ii == 0:
                    break

    dfs(p, cnt + 1)


def select(path=[]):
    if len(path) == N:
        total_path.append(path)
        return

    for i in range(C):
        select(path + [i])

T = int(input())
for tc in range(T):
    N, C, R = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(R)]
    min_ans = R * C

    # 시작 위치 선택하기 column 증복선택 가능, N개
    total_path = []
    select()

    for p in total_path:
        map_copy = copy.deepcopy(MAP)
        dfs(p, 0)




    # for j in range(C):
    #     for i in range(R - 1):
    #         if MAP[i][j] == 0 and MAP[i + 1][j] != 0:
    #             map_copy = MAP[:]
    #             dfs([MAP[i + 1][j], i + 1, j], 0)
    #             break

    print(f'#{tc + 1} {min_ans}')

