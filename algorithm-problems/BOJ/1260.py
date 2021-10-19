# 1260 DFS와 BFS
N, M, V = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    f, t = map(int, input().split())
    edges[f].append(t)
    edges[t].append(f)

visited = [0] * (N+1)
# dfs_arr = [0] * N
dfs_arr = []
def dfs(now, cnt):
    # dfs_arr[cnt] = now
    dfs_arr.append(now)
    edges[now].sort()   # 작은 수 부터 방문

    for t in edges[now]:
        if visited[t] == 1:
            continue
        visited[t] = 1
        dfs(t, cnt+1)

visited[V] = 1
dfs(V, 0)
print(*dfs_arr)

visited = [0] * (N+1)
# bfs_arr = [0] * N
bfs_arr = []
q = [V]
visited[V] = 1
def bfs():
    cnt = 0
    while q:
        now = q.pop(0)
        # bfs_arr[cnt] = now
        bfs_arr.append(now)
        cnt += 1
        edges[now].sort()
        for t in edges[now]:
            if visited[t] == 1:
                continue
            visited[t] = 1
            q.append(t)


bfs()
print(*bfs_arr)