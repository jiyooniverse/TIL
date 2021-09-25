# 12922 이진탐색
T = int(input())

def dfs(now):
    global count
    if now > N:
        return
    dfs(2 * now)
    graph[now] = count
    count += 1
    dfs(2 * now + 1)

for tc in range(T):
    N = int(input())
    graph = [0] * (N + 1)
    count = 1
    dfs(1)

    print(f'#{tc + 1} {graph[1]} {graph[N//2]}')