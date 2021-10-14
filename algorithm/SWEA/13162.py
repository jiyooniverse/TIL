# 13162 최소 신장 트리
# Kruskal's algorithm
def Find(x):
    if parents[x] == x:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px


def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    parents = [i for i in range(V+1)]
    edges = []
    for i in range(E):
        f, t, w = map(int, input().split())
        edges.append([w, f, t])

    # 비용순으로 정렬
    edges.sort()
    #
    total_cost = 0
    for cost, f, t in edges:
        if Find(f) == Find(t):
            continue
        Union(f, t)
        total_cost += cost

    print(f'#{tc + 1} {total_cost}')
