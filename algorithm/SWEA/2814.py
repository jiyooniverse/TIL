#2814 최장 경로

def dfs(now, cnt):
    global max_dist
    max_dist = max(max_dist, cnt)

    for i in range(1, N + 1):
        if arr[now][i] == 1 and check[i] == 0:
            check[i] = 1
            dfs(i, cnt + 1)
            check[i] = 0


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    # 2. DFS 사용
    check = [0] * (N+1)
    max_dist = 0
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x][y] = arr[y][x] = 1   # 2. DFS

    # start 위치 바꿔가면서
    for i in range(1, N+1):
        check[i] = 1
        dfs(i, 1)
        check[i] = 0

    print(f'#{tc + 1} {max_dist}')


