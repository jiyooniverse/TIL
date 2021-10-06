# 2630 색종이
N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]


def dfs(now, k):
    r = now[0]
    c = now[1]

    color = map[r][c]
    flag = 0
    for i in range(r, r + k):
        if flag == 1:
            break
        for j in range(c, c + k):
            # 다 1이면 파란 종이 숫자 하나 증가
            # 다 0이면 흰 종이 숫자 하나 증가

            if map[i][j] != color:
                flag = 1
                # 다르면 4등분 ㄱㄱ
                dfs([r, c], k//2)        # 1번
                dfs([r, c + k//2], k//2)    # 2번
                dfs([r + k//2, c], k // 2)  # 3번
                dfs([r + k//2, c + k//2], k // 2)  # 4번
                break

    if flag == 0:
        colors[color] += 1


colors = [0, 0]
dfs([0, 0], N)

print(colors[0])
print(colors[1])
