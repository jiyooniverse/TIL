# BOJ-10157 자리 배정

C, R = map(int, input().split())    # 가로, 세로
num = int(input())
visited = [[0] * (C+1) for _ in range(R+1)]
dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]
c, r = 1, 0
cnt = 0
d = 0
result = 0
while cnt < num <= C * R:
    cnt += 1
    c += dir_x[d]
    r += dir_y[d]
    visited[r][c] = cnt
    result = f"{c} {r}"
    nr = r + dir_y[d]
    nc = c + dir_x[d]
    if 0 < nc <= C and 0 < nr <= R and visited[nr][nc] == 0:
        continue
    else:
        d = (d + 1) % 4

print(result)

